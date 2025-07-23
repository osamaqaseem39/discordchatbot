"""
Quick setup guide for bot administrators
"""

SETUP_GUIDE = {
    "title": "🛠️ Bot Setup Guide",
    "description": """**Quick Setup for Your Amazon Cashflow Academy Bot:**

**Step 1: Configure Channel Access**
Use `!setchannel` in the channel where you want the bot to work.
Example: `!setchannel #amazon-fba`

**Step 2: Test the Bot**
• Try commands: `!help`, `!research`, `!profit`
• Ask natural questions: "How do I find profitable products?"
• Mention the bot: "@Bot what are Amazon FBA fees?"

**Step 3: Usage Options**
• **Commands**: Use `!command` format for specific functions
• **Natural Chat**: Ask questions directly without commands
• **Mentions**: Tag the bot to get its attention

**Step 4: Monitor Usage (Admin)**
• Use `!stats` to see cache effectiveness and cost savings
• Use `!listchannels` to see configured channels

**Cost Optimization Features:**
• Caching reduces repeat API calls
• Predefined responses for common questions
• Rate limiting prevents overuse
• GPT-4o-mini model for cost efficiency

**Need Help?**
• `!help` - See all commands
• `!about` - Learn about bot features
• Ask questions naturally about Amazon FBA topics!""",
    
    "admin_commands": [
        "`!setchannel` - Configure bot for this channel",
        "`!removechannel` - Remove channel access", 
        "`!listchannels` - View allowed channels",
        "`!stats` - Monitor usage and savings"
    ]
}

def get_setup_guide():
    """Get the setup guide content"""
    return SETUP_GUIDE