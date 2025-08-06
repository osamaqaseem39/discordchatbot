import logging
import os
from datetime import datetime

def setup_logging():
    """Setup logging configuration for the bot"""
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'logs/bot_{datetime.now().strftime("%Y%m%d")}.log'),
            logging.StreamHandler()
        ]
    )
    
    # Set third-party library log levels
    logging.getLogger('discord').setLevel(logging.WARNING)
    logging.getLogger('openai').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    
    logger = logging.getLogger('amazon_cashflow_bot')
    logger.info("Logging system initialized")
    
    return logger

def get_logger(name):
    """Get a logger instance for a specific module"""
    return logging.getLogger(f'amazon_cashflow_bot.{name}')

class BotMetrics:
    """Track bot usage metrics"""
    
    def __init__(self):
        self.logger = get_logger('metrics')
        self.start_time = datetime.now()
        self.command_usage = {}
        self.user_interactions = {}
        self.error_count = 0
        self.successful_requests = 0
    
    def log_command_usage(self, command_name, user_id, guild_id=None):
        """Log command usage statistics"""
        if command_name not in self.command_usage:
            self.command_usage[command_name] = 0
        self.command_usage[command_name] += 1
        
        if user_id not in self.user_interactions:
            self.user_interactions[user_id] = []
        self.user_interactions[user_id].append({
            'command': command_name,
            'timestamp': datetime.now(),
            'guild': guild_id
        })
        
        self.logger.info(f"Command used: {command_name} by user {user_id}")
    
    def log_success(self):
        """Log successful request"""
        self.successful_requests += 1
    
    def log_error(self, error_type, error_message):
        """Log error occurrence"""
        self.error_count += 1
        self.logger.error(f"Error {error_type}: {error_message}")
    
    def get_stats(self):
        """Get current bot statistics"""
        uptime = datetime.now() - self.start_time
        
        return {
            'uptime': str(uptime),
            'total_commands': sum(self.command_usage.values()),
            'unique_users': len(self.user_interactions),
            'successful_requests': self.successful_requests,
            'error_count': self.error_count,
            'most_used_commands': sorted(
                self.command_usage.items(), 
                key=lambda x: x[1], 
                reverse=True
            )[:5]
        }
    
    def get_user_stats(self, user_id):
        """Get statistics for a specific user"""
        if user_id not in self.user_interactions:
            return None
        
        interactions = self.user_interactions[user_id]
        command_counts = {}
        
        for interaction in interactions:
            cmd = interaction['command']
            command_counts[cmd] = command_counts.get(cmd, 0) + 1
        
        return {
            'total_interactions': len(interactions),
            'commands_used': command_counts,
            'first_interaction': interactions[0]['timestamp'] if interactions else None,
            'last_interaction': interactions[-1]['timestamp'] if interactions else None
        }

# Global metrics instance
bot_metrics = BotMetrics()
