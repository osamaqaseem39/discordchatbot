import os

def get_bool_env(var, default):
    val = os.getenv(var)
    if val is None:
        return default
    return val.lower() == 'true'

def get_int_env(var, default):
    val = os.getenv(var)
    if val is None:
        return default
    try:
        return int(val)
    except ValueError:
        return default

def get_float_env(var, default):
    val = os.getenv(var)
    if val is None:
        return default
    try:
        return float(val)
    except ValueError:
        return default

def get_list_env(var, default):
    val = os.getenv(var)
    if val is None or val.strip() == '':
        return default
    return [v.strip() for v in val.split(',') if v.strip()]

# Bot configuration
# BOT_PREFIX, BOT_MAX_RESPONSE_LENGTH, BOT_EMBED_COLOR, BOT_ERROR_COLOR, BOT_WARNING_COLOR, BOT_INFO_COLOR
BOT_CONFIG = {
    'prefix': os.getenv('BOT_PREFIX', '!'),
    'max_response_length': get_int_env('BOT_MAX_RESPONSE_LENGTH', 1000),
    'embed_color': int(os.getenv('BOT_EMBED_COLOR', '0x4CAF50'), 16),
    'error_color': int(os.getenv('BOT_ERROR_COLOR', '0xff6b6b'), 16),
    'warning_color': int(os.getenv('BOT_WARNING_COLOR', '0xffa726'), 16),
    'info_color': int(os.getenv('BOT_INFO_COLOR', '0x2196F3'), 16)
}

# OpenAI configuration
# OPENAI_MODEL, OPENAI_MAX_TOKENS, OPENAI_TEMPERATURE, OPENAI_SYSTEM_PROMPT
OPENAI_CONFIG = {
    'model': os.getenv('OPENAI_MODEL', 'gpt-4o-mini'),
    'max_tokens': get_int_env('OPENAI_MAX_TOKENS', 500),
    'temperature': get_float_env('OPENAI_TEMPERATURE', 0.3),
    'system_prompt': os.getenv('OPENAI_SYSTEM_PROMPT', """
Vous êtes un expert-conseil en entreprise Amazon FBA (Fulfillment by Amazon), en e-commerce et en entrepreneuriat. 
Vous aidez les entrepreneurs à construire des entreprises rentables grâce à :
- Des stratégies de recherche et de sélection de produits
- L'analyse et le calcul des marges bénéficiaires
- La gestion des stocks et l'optimisation des flux de trésorerie
- L'analyse du marché et la recherche de concurrents
- Les stratégies de publicité PPC
- L'approvisionnement et la négociation avec les fournisseurs
- L'optimisation SEO Amazon et des fiches produits
- La gestion des risques et la diversification
- Les stratégies de croissance pour les vendeurs établis
- Les conseils généraux sur l'e-commerce et l'entrepreneuriat

Fournissez toujours des conseils concrets et spécifiques avec des chiffres réels et des exemples lorsque c'est possible. 
Concentrez-vous sur des pratiques commerciales durables et éthiques, et sur la génération de flux de trésorerie à long terme.
Gardez les réponses éducatives et professionnelles, adaptées aussi bien aux débutants qu'aux vendeurs expérimentés.
IMPORTANT : Toutes vos réponses doivent être rédigées en français.
Si la question de l'utilisateur ne concerne pas Amazon FBA, l'e-commerce ou l'entrepreneuriat, répondez poliment : « Je suis spécialisé dans Amazon FBA, l'e-commerce et l'entrepreneuriat. Merci de poser une question en rapport avec ces sujets. »""")
}

# Rate limiting configuration
# RATE_LIMIT_REQUESTS_PER_MINUTE, RATE_LIMIT_REQUESTS_PER_HOUR, RATE_LIMIT_PREMIUM_REQUESTS_PER_MINUTE, RATE_LIMIT_PREMIUM_REQUESTS_PER_HOUR
RATE_LIMIT_CONFIG = {
    'requests_per_minute': get_int_env('RATE_LIMIT_REQUESTS_PER_MINUTE', 5),
    'requests_per_hour': get_int_env('RATE_LIMIT_REQUESTS_PER_HOUR', 25),
    'premium_requests_per_minute': get_int_env('RATE_LIMIT_PREMIUM_REQUESTS_PER_MINUTE', 10),
    'premium_requests_per_hour': get_int_env('RATE_LIMIT_PREMIUM_REQUESTS_PER_HOUR', 50)
}

# Cache configuration
# CACHE_ENABLED, CACHE_TTL_HOURS, CACHE_MAX_ENTRIES
CACHE_CONFIG = {
    'enabled': get_bool_env('CACHE_ENABLED', True),
    'ttl_hours': get_int_env('CACHE_TTL_HOURS', 2),
    'max_entries': get_int_env('CACHE_MAX_ENTRIES', 1000)
}

# Channel configuration
# CHANNEL_RESTRICTED_MODE, CHANNEL_ALLOWED_CHANNELS, CHANNEL_CONVERSATION_MODE, CHANNEL_RESPONSE_TO_MENTIONS
CHANNEL_CONFIG = {
    'restricted_mode': get_bool_env('CHANNEL_RESTRICTED_MODE', True),
    'allowed_channels': get_list_env('CHANNEL_ALLOWED_CHANNELS', []),
    'conversation_mode': get_bool_env('CHANNEL_CONVERSATION_MODE', True),
    'response_to_mentions': get_bool_env('CHANNEL_RESPONSE_TO_MENTIONS', True)
}

# Command categories and descriptions (not env-based)
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

# Educational topics (not env-based)
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
