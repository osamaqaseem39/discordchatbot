import discord
from discord.ext import commands
import asyncio
from openai_service import OpenAIService
from rate_limiter import RateLimiter
from response_cache import response_cache
from predefined_responses import get_predefined_response, search_predefined_responses
from setup_guide import get_setup_guide
from config import BOT_CONFIG, COMMAND_CATEGORIES, EDUCATIONAL_TOPICS, CHANNEL_CONFIG
from logger import get_logger
import json
import random

logger = get_logger(__name__)

# Initialize services
openai_service = OpenAIService()
rate_limiter = RateLimiter()

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx, *, command_name=None):
        """Show help information for commands"""
        if command_name:
            # Show specific command help
            command = self.bot.get_command(command_name)
            if command:
                embed = discord.Embed(
                    title=f"Help: {command.name}",
                    description=command.help or "No description available",
                    color=BOT_CONFIG['info_color']
                )
                embed.add_field(
                    name="Usage",
                    value=f"`{BOT_CONFIG['prefix']}{command.name} {command.signature}`",
                    inline=False
                )
            else:
                embed = discord.Embed(
                    title="❌ Command Not Found",
                    description=f"Command `{command_name}` not found.",
                    color=BOT_CONFIG['error_color']
                )
        else:
            # Show general help
            embed = discord.Embed(
                title="🎓 Amazon Cashflow Academy Bot",
                description="Your AI-powered companion for Amazon FBA education and strategy",
                color=BOT_CONFIG['embed_color']
            )
            
            for category, commands_dict in COMMAND_CATEGORIES.items():
                command_list = []
                for cmd_name, cmd_desc in commands_dict.items():
                    command_list.append(f"`{BOT_CONFIG['prefix']}{cmd_name}` - {cmd_desc}")
                
                embed.add_field(
                    name=f"📁 {category}",
                    value="\n".join(command_list),
                    inline=False
                )
            
            embed.add_field(
                name="💡 Tips",
                value="• Use `!help <command>` for detailed command info\n• Ask questions in natural language\n• Be specific for better responses",
                inline=False
            )
            
        await ctx.send(embed=embed)

    @commands.command(name='about')
    async def about(self, ctx):
        """Information about the Amazon Cashflow Academy bot"""
        embed = discord.Embed(
            title="🏪 Amazon Cashflow Academy Bot",
            description="AI-powered educational companion for Amazon FBA entrepreneurs",
            color=BOT_CONFIG['embed_color']
        )
        
        embed.add_field(
            name="🎯 Mission",
            value="Empowering entrepreneurs with practical Amazon FBA knowledge and cashflow strategies",
            inline=False
        )
        
        embed.add_field(
            name="🔧 Features",
            value="• AI-powered FBA guidance\n• Profit calculations\n• Market analysis\n• Educational content\n• Real-world strategies",
            inline=True
        )
        
        embed.add_field(
            name="📊 Topics Covered",
            value="• Product Research\n• Financial Analysis\n• Business Strategy\n• Scaling & Optimization\n• Risk Management",
            inline=True
        )
        
        embed.set_footer(text="Powered by OpenAI • Built for Amazon FBA success")
        await ctx.send(embed=embed)

    @commands.command(name='stats')
    @commands.has_permissions(administrator=True)
    async def usage_stats(self, ctx):
        """Show bot usage statistics (Admin only)"""
        cache_stats = response_cache.get_cache_stats()
        
        embed = discord.Embed(
            title="📊 Bot Usage Statistics",
            color=BOT_CONFIG['info_color']
        )        
        embed.add_field(
            name="💾 Cache Statistics",
            value=f"Valid Entries: {cache_stats['valid_entries']}\n"
                  f"Expired Entries: {cache_stats['expired_entries']}\n"
                  f"Cache TTL: {cache_stats['cache_ttl_hours']} hours",
            inline=True
        )
        
        embed.add_field(
            name="💰 Cost Savings",
            value=f"API Calls Saved: {cache_stats['valid_entries']}\n"
                  f"Estimated Savings: ~${cache_stats['valid_entries'] * 0.002:.3f}",
            inline=True
        )
        
        await ctx.send(embed=embed)

    @commands.command(name='setchannel')
    @commands.has_permissions(administrator=True)
    async def set_channel(self, ctx, channel: discord.TextChannel = None):
        """Set this channel as the only allowed channel for the bot (Admin only)"""
        if channel is None:
            channel = ctx.channel
        
        # Add channel to allowed list
        if channel.id not in CHANNEL_CONFIG['allowed_channels']:
            CHANNEL_CONFIG['allowed_channels'].append(channel.id)
        
        embed = discord.Embed(
            title="✅ Salon configuré",
            description="Le bot est maintenant limité au salon {channel.mention}\n\nLes utilisateurs peuvent :\n• Utiliser des commandes avec le préfixe !\n• Poser des questions naturellement (je répondrai aux questions sur Amazon FBA)\n• Me mentionner pour attirer mon attention",
            color=BOT_CONFIG['embed_color']
        )
        
        embed.add_field(
            name="💬 Mode Conversation",
            value="Je répondrai aux questions naturelles sur Amazon FBA sans avoir besoin de commandes !",
            inline=False
        )
        
        await ctx.send(embed=embed)

    @commands.command(name='removechannel')
    @commands.has_permissions(administrator=True)  
    async def remove_channel(self, ctx, channel: discord.TextChannel = None):
        """Remove a channel from the allowed list (Admin only)"""
        if channel is None:
            channel = ctx.channel
            
        if channel.id in CHANNEL_CONFIG['allowed_channels']:
            CHANNEL_CONFIG['allowed_channels'].remove(channel.id)
            
            embed = discord.Embed(
                title="❌ Channel Removed",
                description=f"Bot access removed from {channel.mention}",
                color=BOT_CONFIG['warning_color']
            )
        else:
            embed = discord.Embed(
                title="ℹ️ Channel Not Found", 
                description=f"{channel.mention} was not in the allowed channels list",
                color=BOT_CONFIG['info_color']
            )
        
        await ctx.send(embed=embed)

    @commands.command(name='listchannels')
    @commands.has_permissions(administrator=True)
    async def list_channels(self, ctx):
        """List all allowed channels (Admin only)"""
        if not CHANNEL_CONFIG['allowed_channels']:
            embed = discord.Embed(
                title="📋 Allowed Channels",
                description="No channels configured. Use `!setchannel` to add channels.",
                color=BOT_CONFIG['info_color']
            )
        else:
            channel_mentions = []
            for channel_id in CHANNEL_CONFIG['allowed_channels']:
                channel = self.bot.get_channel(channel_id)
                if channel:
                    channel_mentions.append(channel.mention)
                else:
                    channel_mentions.append(f"Unknown Channel (ID: {channel_id})")
            
            embed = discord.Embed(
                title="📋 Allowed Channels",
                description="\n".join(channel_mentions),
                color=BOT_CONFIG['embed_color']
            )
        
        await ctx.send(embed=embed)

    @commands.command(name='setup')
    @commands.has_permissions(administrator=True)
    async def setup_guide(self, ctx):
        """Show bot setup guide (Admin only)"""
        guide = get_setup_guide()
        
        embed = discord.Embed(
            title=guide['title'],
            description=guide['description'],
            color=BOT_CONFIG['embed_color']
        )
        
        embed.add_field(
            name="🔧 Admin Commands",
            value="\n".join(guide['admin_commands']),
            inline=False
        )
        
        embed.set_footer(text="💡 Start with !setchannel to configure your channel")
        await ctx.send(embed=embed)

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Check bot latency"""
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Bot latency: {round(self.bot.latency * 1000)}ms",
            color=BOT_CONFIG['info_color']
        )
        await ctx.send(embed=embed)

class ProductResearchCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='research')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def product_research(self, ctx, *, query=None):
        """Get AI-powered product research guidance"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await self._send_rate_limit_message(ctx)
        
        if not query:
            query = "general product research strategies for Amazon FBA beginners"
        
        prompt = f"Provide detailed Amazon FBA product research guidance for: {query}. Include specific strategies, tools, and actionable steps."
        
        await self._process_ai_request(ctx, prompt, "🔍 Product Research Guidance", "research")

    @commands.command(name='niche')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def niche_analysis(self, ctx, *, niche=None):
        """Analyze market niches and opportunities"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await self._send_rate_limit_message(ctx)
        
        if not niche:
            embed = discord.Embed(
                title="❓ Niche Analysis",
                description="Please specify a niche or category to analyze.\n\nExample: `!niche kitchen gadgets`",
                color=BOT_CONFIG['warning_color']
            )
            return await ctx.send(embed=embed)
        
        prompt = f"Analyze the '{niche}' market niche for Amazon FBA opportunities. Include market size, competition level, profit potential, trends, and specific product suggestions."
        
        await self._process_ai_request(ctx, prompt, f"🎯 Niche Analysis: {niche}", "niche")

    @commands.command(name='competition')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def competition_analysis(self, ctx, *, product=None):
        """Get competitive analysis strategies"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await self._send_rate_limit_message(ctx)
        
        if not product:
            product = "general product category"
        
        prompt = f"Explain how to conduct competitive analysis for '{product}' on Amazon. Include tools, metrics to track, pricing strategies, and differentiation opportunities."
        
        await self._process_ai_request(ctx, prompt, "⚔️ Competitive Analysis", "competition")

    async def _process_ai_request(self, ctx, prompt, title, command_type="general"):
        """Process AI request with error handling and predefined response checking"""
        # Check for predefined responses first to save API calls
        predefined_key = search_predefined_responses(prompt)
        if predefined_key:
            predefined = get_predefined_response(predefined_key)
            if predefined:
                embed = discord.Embed(
                    title=predefined['title'],
                    description=predefined['content'],
                    color=BOT_CONFIG['embed_color']
                )
                embed.set_footer(text="💡 Quick response - No API usage • Ask follow-up questions for more specific guidance")
                return await ctx.send(embed=embed)
        
        async with ctx.typing():
            try:
                response = await openai_service.get_educational_response(prompt, command_type)
                
                if len(response) > BOT_CONFIG['max_response_length']:
                    # Split long responses
                    chunks = [response[i:i+BOT_CONFIG['max_response_length']] 
                             for i in range(0, len(response), BOT_CONFIG['max_response_length'])]
                    
                    for i, chunk in enumerate(chunks):
                        embed = discord.Embed(
                            title=f"{title} (Part {i+1}/{len(chunks)})",
                            description=chunk,
                            color=BOT_CONFIG['embed_color']
                        )
                        await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title=title,
                        description=response,
                        color=BOT_CONFIG['embed_color']
                    )
                    embed.set_footer(text="💡 Ask follow-up questions for more specific guidance")
                    await ctx.send(embed=embed)
                    
            except Exception as e:
                logger.error(f"Error processing AI request: {e}")
                embed = discord.Embed(
                    title="❌ Service Unavailable",
                    description="Unable to process your request right now. Please try again later.",
                    color=BOT_CONFIG['error_color']
                )
                await ctx.send(embed=embed)

    async def _send_rate_limit_message(self, ctx):
        """Send rate limit exceeded message"""
        embed = discord.Embed(
            title="⏰ Rate Limit Exceeded",
            description="You've reached your request limit. Please wait before making another request.",
            color=BOT_CONFIG['warning_color']
        )
        await ctx.send(embed=embed)

class FinancialCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='profit')
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def profit_calculator(self, ctx, selling_price: float = None, cost: float = None, *, additional_info=None):
        """Calculate profit margins and provide financial analysis"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await ProductResearchCommands._send_rate_limit_message(self, ctx)
        
        if selling_price and cost:
            prompt = f"Calculate detailed Amazon FBA profit analysis for a product with selling price ${selling_price} and cost ${cost}. Include all Amazon fees, shipping, storage, and provide ROI analysis. {additional_info or ''}"
        else:
            prompt = "Explain Amazon FBA profit calculation methodology, including all fees, costs, and provide examples with different product scenarios."
        
        await ProductResearchCommands._process_ai_request(self, ctx, prompt, "💰 Profit Analysis")

    @commands.command(name='cashflow')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def cashflow_analysis(self, ctx, *, scenario=None):
        """Analyze cashflow projections and management strategies"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await ProductResearchCommands._send_rate_limit_message(self, ctx)
        
        if scenario:
            prompt = f"Provide detailed Amazon FBA cashflow analysis for this scenario: {scenario}. Include projections, management strategies, and risk mitigation."
        else:
            prompt = "Explain Amazon FBA cashflow management strategies, including inventory cycles, working capital requirements, and optimization techniques."
        
        await ProductResearchCommands._process_ai_request(self, ctx, prompt, "💵 Cashflow Analysis")

    @commands.command(name='fees')
    async def amazon_fees(self, ctx, *, category=None):
        """Understand Amazon FBA fees and calculations"""
        prompt = f"Explain Amazon FBA fee structure in detail{'for ' + category + ' products' if category else ''}. Include referral fees, FBA fees, storage costs, and provide calculation examples."
        
        await ProductResearchCommands._process_ai_request(self, ctx, prompt, "📋 Amazon FBA Fees")

class BusinessStrategyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='launch')
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def product_launch(self, ctx, *, product_type=None):
        """Get product launch strategies and timelines"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await ProductResearchCommands._send_rate_limit_message(self, ctx)
        
        if product_type:
            prompt = f"Create a comprehensive Amazon FBA product launch strategy for {product_type}. Include timeline, budget considerations, marketing tactics, and success metrics."
        else:
            prompt = "Provide a detailed Amazon FBA product launch framework including pre-launch preparation, launch strategies, and post-launch optimization."
        
        await ProductResearchCommands._process_ai_request(self, ctx, prompt, "🚀 Product Launch Strategy")

    @commands.command(name='scale')
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def scaling_strategies(self, ctx, *, current_situation=None):
        """Learn how to scale your Amazon business"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await ProductResearchCommands._send_rate_limit_message(self, ctx)
        
        if current_situation:
            prompt = f"Provide Amazon FBA scaling strategies for this situation: {current_situation}. Include growth tactics, resource allocation, and risk management."
        else:
            prompt = "Explain comprehensive Amazon FBA business scaling strategies, including product line expansion, market diversification, and operational optimization."
        
        await ProductResearchCommands._process_ai_request(self, ctx, prompt, "📈 Scaling Strategies")

    @commands.command(name='optimize')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def optimization_guide(self, ctx, *, focus_area=None):
        """Optimize listings and advertising performance"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await ProductResearchCommands._send_rate_limit_message(self, ctx)
        
        if focus_area:
            prompt = f"Provide detailed optimization strategies for {focus_area} in Amazon FBA. Include specific tactics, metrics to track, and improvement methodologies."
        else:
            prompt = "Explain comprehensive Amazon FBA optimization strategies covering listings, PPC advertising, inventory management, and conversion rate improvement."
        
        await ProductResearchCommands._process_ai_request(self, ctx, prompt, "⚡ Optimization Guide")

class EducationalCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='learn')
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def learn_topic(self, ctx, *, topic=None):
        """Get educational content on specific FBA topics"""
        if not topic:
            embed = discord.Embed(
                title="📚 Available Learning Topics",
                description="Choose a topic to learn about:",
                color=BOT_CONFIG['info_color']
            )
            
            # Display available topics
            topics_text = "\n".join([f"• {topic}" for topic in EDUCATIONAL_TOPICS[:10]])
            topics_text += f"\n... and {len(EDUCATIONAL_TOPICS) - 10} more topics!"
            
            embed.add_field(
                name="Popular Topics",
                value=topics_text,
                inline=False
            )
            
            embed.add_field(
                name="Usage",
                value=f"`{BOT_CONFIG['prefix']}learn <topic>`\nExample: `{BOT_CONFIG['prefix']}learn product research`",
                inline=False
            )
            
            return await ctx.send(embed=embed)
        
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await ProductResearchCommands._send_rate_limit_message(self, ctx)
        
        prompt = f"Provide comprehensive educational content about '{topic}' for Amazon FBA sellers. Include fundamentals, advanced strategies, tools, and practical examples."
        
        await ProductResearchCommands._process_ai_request(self, ctx, prompt, f"📚 Learning: {topic.title()}")

    @commands.command(name='case')
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def case_study(self, ctx, *, scenario=None):
        """Request case studies and real-world examples"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await ProductResearchCommands._send_rate_limit_message(self, ctx)
        
        if scenario:
            prompt = f"Create a detailed Amazon FBA case study based on this scenario: {scenario}. Include background, strategy, implementation, results, and lessons learned."
        else:
            prompt = "Provide an educational Amazon FBA case study example showing the complete journey from product research to successful launch, including challenges and solutions."
        
        await ProductResearchCommands._process_ai_request(self, ctx, prompt, "📊 Case Study Analysis")

    @commands.command(name='trends')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def market_trends(self, ctx, *, market=None):
        """Learn about current Amazon marketplace trends"""
        if not await rate_limiter.check_rate_limit(ctx.author.id):
            return await ProductResearchCommands._send_rate_limit_message(self, ctx)
        
        if market:
            prompt = f"Analyze current Amazon marketplace trends for {market}. Include emerging opportunities, changing consumer behavior, and strategic recommendations."
        else:
            prompt = "Provide an overview of current Amazon FBA marketplace trends, including emerging categories, policy changes, and strategic opportunities for sellers."
        
        await ProductResearchCommands._process_ai_request(self, ctx, prompt, "📈 Market Trends Analysis")

# Natural language processing command
@commands.Cog.listener()
async def on_message(message):
    """Handle natural language questions"""
    if message.author.bot or not message.content or message.content.startswith(BOT_CONFIG['prefix']):
        return
    
    # Check if message mentions the bot or is a DM
    if message.guild and not (message.mentions and message.mentions[0] == message.guild.me):
        return
    
    # Check rate limiting
    if not await rate_limiter.check_rate_limit(message.author.id):
        return
    
    # Process natural language query
    async with message.channel.typing():
        try:
            # Clean the message content
            content = message.content
            if message.mentions:
                for mention in message.mentions:
                    content = content.replace(f'<@{mention.id}>', '').strip()
            
            prompt = f"User question about Amazon FBA: {content}. Provide helpful, educational guidance."
            response = await openai_service.get_educational_response(prompt)
            
            embed = discord.Embed(
                title="🤖 AI Assistant",
                description=response[:BOT_CONFIG['max_response_length']],
                color=BOT_CONFIG['embed_color']
            )
            embed.set_footer(text="💡 Use specific commands for detailed guidance")
            
            await message.reply(embed=embed)
            
        except Exception as e:
            logger.error(f"Error processing natural language query: {e}")

async def setup_commands(bot):
    """Setup all command cogs"""
    await bot.add_cog(GeneralCommands(bot))
    await bot.add_cog(ProductResearchCommands(bot))
    await bot.add_cog(FinancialCommands(bot))
    await bot.add_cog(BusinessStrategyCommands(bot))
    await bot.add_cog(EducationalCommands(bot))
    
    logger.info("All command cogs loaded successfully")
