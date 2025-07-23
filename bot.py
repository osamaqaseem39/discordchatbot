import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from commands import setup_commands
from logger import setup_logging
from config import BOT_CONFIG, CHANNEL_CONFIG
from openai_service import OpenAIService
import aiohttp
from datetime import timezone

# Load environment variables
load_dotenv()

# Setup logging
logger = setup_logging()

# Initialize OpenAI service for conversational mode
openai_service = OpenAIService()

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(
    command_prefix=BOT_CONFIG['prefix'],
    intents=intents,
    help_command=None,
    description="Amazon Cashflow Academy - Your AI-powered FBA education companion"
)

@bot.event
async def on_ready():
    """Event triggered when bot is ready"""
    logger.info(f'{bot.user} s\'est connecté à Discord!')
    logger.info(f'Le bot est actif dans {len(bot.guilds)} serveurs')
    
    # Set bot status
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="Stratégies Amazon FBA | !help"
    )
    await bot.change_presence(activity=activity)

@bot.event
async def on_command_error(ctx, error):
    """Global error handler"""
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="❌ Commande introuvable",
            description=f"La commande `{ctx.message.content.split()[0]}` n'est pas reconnue. Utilisez `!help` pour voir les commandes disponibles.",
            color=0xff6b6b
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="❌ Argument manquant",
            description=f"Argument requis manquant : `{error.param.name}`. Utilisez `!help {ctx.command}` pour plus d'informations.",
            color=0xff6b6b
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="⏰ Commande en cooldown",
            description=f"Veuillez attendre {error.retry_after:.1f} secondes avant de réutiliser cette commande.",
            color=0xffa726
        )
        await ctx.send(embed=embed)
    else:
        logger.error(f"Erreur non gérée dans la commande {ctx.command}: {error}")
        embed = discord.Embed(
            title="❌ Une erreur est survenue",
            description="Une erreur s'est produite lors du traitement de votre demande. Veuillez réessayer plus tard.",
            color=0xff6b6b
        )
        await ctx.send(embed=embed)

def is_allowed_channel(channel_id):
    """Check if the channel is allowed for bot interactions"""
    if not CHANNEL_CONFIG['restricted_mode']:
        return True
    return channel_id in CHANNEL_CONFIG['allowed_channels']

# --- Verification Bot Logic ---
VERIFICATION_CHANNEL_NAME = 'verify'
VERIFIED_ROLE_NAME = 'Vérifié'
QUESTIONS = [
    ("interest", "Qu'est-ce qui vous intéresse le plus dans Amazon FBA ?"),
    ("experience", "Avez-vous déjà essayé Amazon FBA ?"),
    ("challenge", "Quel est votre plus grand défi avec FBA en ce moment ?"),
    ("status", "Vendez-vous actuellement ou êtes-vous en phase de recherche ?")
]

pending_verifications = {}  # user_id: { 'step': int, 'answers': {key: answer}, 'message_ids': [int] }

@bot.event
async def on_member_join(member):
    # Find the verification channel
    channel = discord.utils.get(member.guild.text_channels, name=VERIFICATION_CHANNEL_NAME)
    if not channel:
        logger.error(f"Le canal de vérification '{VERIFICATION_CHANNEL_NAME}' est introuvable.")
        return
    # Start verification process
    mention = member.mention
    msg = await channel.send(f"Bienvenue {mention} ! Merci de répondre aux questions suivantes pour être vérifié(e).")
    # Ask the first question
    q_key, q_text = QUESTIONS[0]
    q_msg = await channel.send(f"{mention} {q_text}")
    pending_verifications[member.id] = {
        'step': 0,
        'answers': {},
        'message_ids': [msg.id, q_msg.id]
    }

@bot.event
async def on_message(message):
    """Event triggered on every message"""
    if message.author == bot.user:
        return
    
    # Allow admin setup commands everywhere if no channels are configured yet
    is_setup_command = message.content.startswith('!setchannel') or message.content.startswith('!setup') or message.content.startswith('!help')
    
    # Check if channel is allowed (or if it's a setup command and no channels configured)
    if not is_allowed_channel(message.channel.id):
        if not (is_setup_command and len(CHANNEL_CONFIG['allowed_channels']) == 0):
            return
    
    # Log user interactions
    if message.content.startswith(BOT_CONFIG['prefix']):
        logger.info(f"Commande utilisée par {message.author}: {message.content}")
    
    # Process commands first
    await bot.process_commands(message)
    
    # If no command was processed and conversation mode is enabled
    if CHANNEL_CONFIG['conversation_mode'] and not message.content.startswith(BOT_CONFIG['prefix']):
        # Check if bot was mentioned or if it's a question/request
        bot_mentioned = bot.user.mentioned_in(message)
        looks_like_question = any(word in message.content.lower() for word in 
                                ['?', 'how', 'what', 'why', 'when', 'where', 'help', 'can you', 'amazon', 'fba', 'profit', 'sell'])
        
        if bot_mentioned or looks_like_question:
            await handle_natural_conversation(message)

    # Verification logic
    if message.channel.name == VERIFICATION_CHANNEL_NAME:
        user_id = message.author.id
        if user_id in pending_verifications:
            state = pending_verifications[user_id]
            step = state['step']
            if message.reference and message.reference.message_id not in state['message_ids']:
                return  # Only allow replies to the bot's question messages
            # Store answer
            q_key, _ = QUESTIONS[step]
            state['answers'][q_key] = message.content.strip()
            state['step'] += 1
            # Next question or finish
            if state['step'] < len(QUESTIONS):
                next_q_key, next_q_text = QUESTIONS[state['step']]
                q_msg = await message.channel.send(f"{message.author.mention} {next_q_text}")
                state['message_ids'].append(q_msg.id)
            else:
                # Assign role
                role = discord.utils.get(message.guild.roles, name=VERIFIED_ROLE_NAME)
                if role:
                    await message.author.add_roles(role, reason="Vérification complétée")
                # Gather info
                join_date = member_join_date_utc(message.author)
                data = {
                    "username": str(message.author),
                    "user_id": str(message.author.id),
                    "join_date": join_date,
                    "answers": state['answers']
                }
                # DM user
                try:
                    await message.author.send("Vous êtes maintenant vérifié(e) ! Bienvenue 🎉")
                except Exception as e:
                    logger.warning(f"Impossible d'envoyer un message privé à l'utilisateur {message.author}: {e}")
                # Send to GoHighLevel webhook
                webhook_url = os.getenv('GOHIGHLEVEL_WEBHOOK_URL')
                if webhook_url:
                    async with aiohttp.ClientSession() as session:
                        try:
                            await session.post(webhook_url, json=data)
                        except Exception as e:
                            logger.error(f"Échec de l'envoi des données de vérification: {e}")
                else:
                    logger.error("GOHIGHLEVEL_WEBHOOK_URL non défini dans les variables d'environnement.")
                # Cleanup
                del pending_verifications[user_id]
                await message.channel.send(f"{message.author.mention} Vous êtes maintenant vérifié(e) !")
                return
            return  # Don't process as command or conversation

async def handle_natural_conversation(message):
    """Handle natural conversation without command prefix"""
    try:
        async with message.channel.typing():
            # Clean the message content (remove mentions)
            content = message.content
            if bot.user.mentioned_in(message):
                content = content.replace(f'<@{bot.user.id}>', '').strip()
            
            # Add instruction to limit answer length
            prompt = (
                f"L'utilisateur a demandé : {content}. Fournissez une réponse utile liée à Amazon FBA. "
                f"Veuillez répondre en moins de 1000 caractères ou 150 mots."
            )
            
            # Get AI response for natural conversation
            response = await openai_service.get_educational_response(
                prompt, 
                "conversation"
            )
            
            # Limit response to 1000 characters and send as a single message
            trimmed_response = response[:1000]
            await message.reply(trimmed_response)
            
    except Exception as e:
        logger.error(f"Erreur dans la conversation naturelle: {e}")
        await message.reply("Désolé, je ne peux pas traiter votre question pour le moment. Essayez d'utiliser une commande comme `!help`.")

async def main():
    """Main function to start the bot"""
    async with bot:
        # Setup commands
        await setup_commands(bot)
        
        # Get Discord token
        token = os.getenv('DISCORD_TOKEN')
        if not token:
            logger.error("DISCORD_TOKEN non trouvé dans les variables d'environnement")
            return
        
        try:
            await bot.start(token)
        except discord.LoginFailure:
            logger.error("Jeton Discord invalide fourni")
        except Exception as e:
            logger.error(f"Échec du démarrage du bot: {e}")

def member_join_date_utc(member):
    # Returns ISO 8601 UTC join date
    if hasattr(member, 'joined_at') and member.joined_at:
        return member.joined_at.astimezone(timezone.utc).isoformat()
    return None

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot arrêté par l'utilisateur")
    except Exception as e:
        logger.error(f"Erreur critique: {e}")
