import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from commands import setup_commands
from logger import setup_logging
from config import BOT_CONFIG, CHANNEL_CONFIG
from openai_service import OpenAIService

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
    logger.info(f'{bot.user} has connected to Discord!')
    logger.info(f'Bot is active in {len(bot.guilds)} guilds')
    
    # Set bot status
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="Amazon FBA strategies | !help"
    )
    await bot.change_presence(activity=activity)

@bot.event
async def on_command_error(ctx, error):
    """Global error handler"""
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="❌ Command Not Found",
            description=f"Command `{ctx.message.content.split()[0]}` not recognized. Use `!help` for available commands.",
            color=0xff6b6b
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="❌ Missing Arguments",
            description=f"Missing required argument: `{error.param.name}`. Use `!help {ctx.command}` for usage info.",
            color=0xff6b6b
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="⏰ Command on Cooldown",
            description=f"Please wait {error.retry_after:.1f} seconds before using this command again.",
            color=0xffa726
        )
        await ctx.send(embed=embed)
    else:
        logger.error(f"Unhandled error in command {ctx.command}: {error}")
        embed = discord.Embed(
            title="❌ An Error Occurred",
            description="Something went wrong while processing your request. Please try again later.",
            color=0xff6b6b
        )
        await ctx.send(embed=embed)

def is_allowed_channel(channel_id):
    """Check if the channel is allowed for bot interactions"""
    if not CHANNEL_CONFIG['restricted_mode']:
        return True
    return channel_id in CHANNEL_CONFIG['allowed_channels']

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
        logger.info(f"Command used by {message.author}: {message.content}")
    
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

async def handle_natural_conversation(message):
    """Handle natural conversation without command prefix"""
    try:
        async with message.channel.typing():
            # Clean the message content (remove mentions)
            content = message.content
            if bot.user.mentioned_in(message):
                content = content.replace(f'<@{bot.user.id}>', '').strip()
            
            # Get AI response for natural conversation
            response = await openai_service.get_educational_response(
                f"User asked: {content}. Provide a helpful Amazon FBA related response.", 
                "conversation"
            )
            
            # Send response (split if too long)
            if len(response) > BOT_CONFIG['max_response_length']:
                # Split long responses at complete sentences or logical breaks
                chunks = []
                current_chunk = ""
                
                # Split by sentences first, then by paragraphs
                sentences = response.split('. ')
                paragraphs = response.split('\n\n')
                
                # Use paragraphs if they're more logical, otherwise use sentences
                if len(paragraphs) > 1 and any(len(p) > 100 for p in paragraphs):
                    split_points = paragraphs
                else:
                    split_points = sentences
                
                for i, part in enumerate(split_points):
                    # Add period back if we split by sentences
                    if split_points == sentences and i < len(split_points) - 1:
                        part += '. '
                    
                    # If adding this part would exceed limit, start new chunk
                    if len(current_chunk + part) > BOT_CONFIG['max_response_length']:
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                            current_chunk = part
                        else:
                            # If single part is too long, split at word boundary
                            words = part.split()
                            temp_chunk = ""
                            for word in words:
                                if len(temp_chunk + " " + word) <= BOT_CONFIG['max_response_length']:
                                    temp_chunk += " " + word if temp_chunk else word
                                else:
                                    if temp_chunk:
                                        chunks.append(temp_chunk.strip())
                                    temp_chunk = word
                            if temp_chunk:
                                current_chunk = temp_chunk
                    else:
                        current_chunk += part
                
                # Add the last chunk
                if current_chunk:
                    chunks.append(current_chunk.strip())
                
                for chunk in chunks:
                    await message.reply(chunk)
            else:
                await message.reply(response)
                
    except Exception as e:
        logger.error(f"Error in natural conversation: {e}")
        await message.reply("Sorry, I couldn't process your question right now. Try using a command like `!help` instead.")

async def main():
    """Main function to start the bot"""
    async with bot:
        # Setup commands
        await setup_commands(bot)
        
        # Get Discord token
        token = os.getenv('DISCORD_TOKEN')
        if not token:
            logger.error("DISCORD_TOKEN not found in environment variables")
            return
        
        try:
            await bot.start(token)
        except discord.LoginFailure:
            logger.error("Invalid Discord token provided")
        except Exception as e:
            logger.error(f"Failed to start bot: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot shutdown by user")
    except Exception as e:
        logger.error(f"Critical error: {e}")
