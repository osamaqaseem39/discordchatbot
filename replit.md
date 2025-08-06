# Amazon Cashflow Academy Discord Bot

## Overview

This is a Discord bot designed to provide AI-powered Amazon FBA (Fulfillment by Amazon) education and strategy guidance. The bot leverages OpenAI's GPT-4o model to deliver expert advice on Amazon business strategies, product research, cashflow optimization, and more.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Discord Bot Interface**: Built using the discord.py library with command-based interactions
- **Command System**: Modular command structure using Discord.py's Cogs system
- **Embedded Responses**: Rich Discord embeds for better user experience with color-coded messages

### Backend Architecture
- **Python-based**: Core application written in Python using async/await patterns
- **Modular Design**: Separated concerns with distinct modules for commands, logging, rate limiting, and AI services
- **Event-driven**: Discord event handlers for bot lifecycle management

### AI Integration
- **OpenAI Service**: Dedicated service class for GPT-4o API interactions
- **Specialized Prompts**: Amazon FBA-focused system prompts for contextual responses
- **Async Processing**: Non-blocking AI request handling using thread pool execution

## Key Components

### 1. Bot Core (`bot.py`)
- Discord bot initialization with proper intents
- Event handlers for ready state and error management
- Status activity configuration
- Global command error handling

### 2. Command System (`commands.py`)
- Modular command structure using Discord Cogs
- Help command system with category-based organization
- Integration with AI service for educational responses

### 3. OpenAI Service (`openai_service.py`)
- Wrapper around OpenAI API client
- Async request handling with proper error management
- Amazon FBA-specialized system prompts
- Thread pool execution for synchronous API calls

### 4. Rate Limiting (`rate_limiter.py`)
- User-based request tracking
- Premium tier support with higher limits
- Time-based cleanup of old requests
- Configurable limits per minute/hour

### 5. Logging System (`logger.py`)
- Structured logging with file and console output
- Daily log rotation
- Metrics tracking for bot usage
- Third-party library log level management

### 6. Configuration (`config.py`)
- Centralized configuration management
- Bot settings (prefixes, colors, limits)
- OpenAI model configuration (GPT-4o)
- Rate limiting parameters

## Data Flow

1. **User Input**: Discord user sends command with bot prefix
2. **Command Processing**: Discord.py routes command to appropriate handler
3. **Rate Limiting**: Check user's request limits before processing
4. **AI Processing**: Forward educational queries to OpenAI service
5. **Response Generation**: Format AI response into Discord embed
6. **Logging**: Track usage metrics and log interactions
7. **Response Delivery**: Send formatted response back to Discord channel

## External Dependencies

### Required Services
- **Discord API**: Bot hosting and user interaction
- **OpenAI API**: GPT-4o model for AI-powered responses

### Python Libraries
- `discord.py`: Discord bot framework
- `openai`: Official OpenAI Python client
- `python-dotenv`: Environment variable management
- `asyncio`: Asynchronous programming support

### Environment Variables
- `DISCORD_TOKEN`: Bot authentication token
- `OPENAI_API_KEY`: OpenAI API access key

## Deployment Strategy

### Environment Setup
- Python environment with required dependencies
- Environment variables configuration
- Log directory creation for file logging

### Bot Configuration
- Discord application and bot setup
- Proper intent configuration for message content access
- Guild permissions for bot functionality

### Scaling Considerations
- Rate limiting prevents API abuse
- Premium user tier system for enhanced limits
- Modular architecture supports feature expansion
- Logging system enables monitoring and debugging

### Security Features
- Environment variable-based secret management
- Rate limiting to prevent abuse
- Error handling to prevent information leakage
- Structured logging for audit trails

## Recent Changes

### July 21, 2025 - Cost Optimization & Channel Restrictions
- **Model Change**: Switched from GPT-4o to GPT-4o-mini for 60% cost reduction
- **Token Limits**: Reduced max_tokens from 1000 to 500 to minimize usage
- **Response Caching**: Implemented 2-hour cache system to avoid duplicate API calls
- **Rate Limiting**: Reduced user limits (5/min, 25/hour) to control costs
- **Predefined Responses**: Added instant responses for common questions (research, fees, profit, launch)
- **Channel Restrictions**: Bot now works only in admin-configured channels
- **Natural Conversation**: Users can ask questions without commands in allowed channels
- **Admin Tools**: Added channel management commands and usage statistics

## Key Features

### Channel Management
- **Restricted Access**: Bot only responds in admin-configured channels
- **Setup Commands**: `!setchannel`, `!removechannel`, `!listchannels`
- **Natural Conversation**: Users can ask questions without command prefixes
- **Mention Support**: Bot responds when mentioned in allowed channels

### Cost Optimization
- **GPT-4o-mini Model**: 60% cheaper than GPT-4o
- **Response Caching**: 2-hour cache prevents duplicate API calls  
- **Predefined Responses**: Instant answers for common questions
- **Rate Limiting**: Controlled usage to prevent overuse

## Setup Instructions

1. **Configure Channel**: Admin uses `!setchannel` in desired channel
2. **Test Commands**: Try `!help`, `!research`, `!profit`
3. **Natural Chat**: Ask "How do I find profitable products?"
4. **Monitor Usage**: Use `!stats` to track cost savings

## Development Notes

- Response caching system prevents duplicate API calls for similar queries
- Predefined responses handle common questions without API usage
- Architecture supports easy addition of new command categories
- Premium user system is implemented but requires database integration for persistence
- Metrics system tracks usage and can be extended for analytics