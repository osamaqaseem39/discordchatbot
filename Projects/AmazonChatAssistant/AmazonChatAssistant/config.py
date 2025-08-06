import os

# Bot configuration
BOT_CONFIG = {
    'prefix': '!',
    'max_response_length': 2000,
    'embed_color': 0x4CAF50,
    'error_color': 0xff6b6b,
    'warning_color': 0xffa726,
    'info_color': 0x2196F3
}

# OpenAI configuration
OPENAI_CONFIG = {
    'model': 'gpt-4o-mini',  # Using the more cost-effective gpt-4o-mini model
    'max_tokens': 500,  # Reduced from 1000 to save costs
    'temperature': 0.3,  # Lower temperature for more consistent responses
    'system_prompt': """You are an expert Amazon FBA (Fulfillment by Amazon) business advisor and cashflow strategist. 
    You help entrepreneurs build profitable Amazon businesses through:
    
    - Product research and selection strategies
    - Profit margin analysis and calculations
    - Inventory management and cashflow optimization
    - Market analysis and competitor research
    - PPC advertising strategies
    - Supplier sourcing and negotiation
    - Amazon SEO and listing optimization
    - Risk management and diversification
    - Scaling strategies for established sellers
    
    Always provide actionable, specific advice with real numbers and examples when possible. 
    Focus on sustainable, ethical business practices and long-term cashflow generation.
    Keep responses educational and professional, suitable for both beginners and experienced sellers."""
}

# Rate limiting configuration - Reduced to save API costs
RATE_LIMIT_CONFIG = {
    'requests_per_minute': 5,  # Reduced from 10
    'requests_per_hour': 25,   # Reduced from 50
    'premium_requests_per_minute': 10,  # Reduced from 20
    'premium_requests_per_hour': 50     # Reduced from 100
}

# Cache configuration
CACHE_CONFIG = {
    'enabled': True,
    'ttl_hours': 2,  # Cache responses for 2 hours
    'max_entries': 1000
}

# Channel configuration
CHANNEL_CONFIG = {
    'restricted_mode': True,  # Only work in specific channels
    'allowed_channels': [],   # Will be populated by admin commands
    'conversation_mode': True,  # Allow natural conversation without prefix
    'response_to_mentions': True  # Respond when mentioned
}

# Command categories and descriptions
COMMAND_CATEGORIES = {
    'General': {
        'help': 'Show available commands and usage information',
        'about': 'Learn about the Amazon Cashflow Academy bot',
        'ping': 'Check bot responsiveness'
    },
    'Admin': {
        'setchannel': 'Restrict bot to specific channel (Admin)',
        'removechannel': 'Remove channel restriction (Admin)',
        'listchannels': 'List allowed channels (Admin)',
        'stats': 'Show usage statistics (Admin)'
    },
    'Product Research': {
        'research': 'Get guidance on product research strategies',
        'niche': 'Analyze market niches and opportunities',
        'competition': 'Understand competitive analysis techniques'
    },
    'Financial Analysis': {
        'profit': 'Calculate profit margins and ROI',
        'cashflow': 'Analyze cashflow projections and management',
        'fees': 'Understand Amazon FBA fees and calculations'
    },
    'Business Strategy': {
        'launch': 'Get product launch strategies and timelines',
        'scale': 'Learn how to scale your Amazon business',
        'optimize': 'Optimize listings and advertising performance'
    },
    'Education': {
        'learn': 'Get educational content on specific FBA topics',
        'case': 'Request case studies and real-world examples',
        'trends': 'Learn about current Amazon marketplace trends'
    }
}

# Educational topics
EDUCATIONAL_TOPICS = [
    'product research methods',
    'profit margin calculations',
    'Amazon PPC strategies',
    'inventory management',
    'supplier sourcing',
    'listing optimization',
    'keyword research',
    'competitive analysis',
    'cashflow forecasting',
    'risk management',
    'scaling strategies',
    'market trends',
    'Amazon policies',
    'brand building',
    'international expansion'
]
