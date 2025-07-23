import time
from collections import defaultdict
from config import RATE_LIMIT_CONFIG
from logger import get_logger

logger = get_logger(__name__)

class RateLimiter:
    def __init__(self):
        self.user_requests = defaultdict(list)
        self.premium_users = set()  # Could be loaded from database
        
    def add_premium_user(self, user_id):
        """Add user to premium tier"""
        self.premium_users.add(user_id)
        logger.info(f"User {user_id} added to premium tier")
    
    def remove_premium_user(self, user_id):
        """Remove user from premium tier"""
        self.premium_users.discard(user_id)
        logger.info(f"User {user_id} removed from premium tier")
    
    async def check_rate_limit(self, user_id):
        """Check if user has exceeded rate limits"""
        current_time = time.time()
        
        # Clean old requests (older than 1 hour)
        self._clean_old_requests(user_id, current_time)
        
        user_requests = self.user_requests[user_id]
        
        # Determine limits based on user tier
        if user_id in self.premium_users:
            minute_limit = RATE_LIMIT_CONFIG['premium_requests_per_minute']
            hour_limit = RATE_LIMIT_CONFIG['premium_requests_per_hour']
        else:
            minute_limit = RATE_LIMIT_CONFIG['requests_per_minute']
            hour_limit = RATE_LIMIT_CONFIG['requests_per_hour']
        
        # Count requests in the last minute
        minute_ago = current_time - 60
        recent_requests = [req_time for req_time in user_requests if req_time > minute_ago]
        
        # Check minute limit
        if len(recent_requests) >= minute_limit:
            logger.warning(f"User {user_id} exceeded minute rate limit")
            return False
        
        # Check hour limit
        if len(user_requests) >= hour_limit:
            logger.warning(f"User {user_id} exceeded hour rate limit")
            return False
        
        # Add current request
        user_requests.append(current_time)
        return True
    
    def _clean_old_requests(self, user_id, current_time):
        """Remove requests older than 1 hour"""
        hour_ago = current_time - 3600
        self.user_requests[user_id] = [
            req_time for req_time in self.user_requests[user_id] 
            if req_time > hour_ago
        ]
    
    def get_user_stats(self, user_id):
        """Get current usage stats for a user"""
        current_time = time.time()
        self._clean_old_requests(user_id, current_time)
        
        user_requests = self.user_requests[user_id]
        
        # Count requests in last minute and hour
        minute_ago = current_time - 60
        minute_requests = len([req for req in user_requests if req > minute_ago])
        hour_requests = len(user_requests)
        
        # Get limits
        if user_id in self.premium_users:
            minute_limit = RATE_LIMIT_CONFIG['premium_requests_per_minute']
            hour_limit = RATE_LIMIT_CONFIG['premium_requests_per_hour']
            tier = "Premium"
        else:
            minute_limit = RATE_LIMIT_CONFIG['requests_per_minute']
            hour_limit = RATE_LIMIT_CONFIG['requests_per_hour']
            tier = "Standard"
        
        return {
            'tier': tier,
            'minute_requests': minute_requests,
            'minute_limit': minute_limit,
            'hour_requests': hour_requests,
            'hour_limit': hour_limit,
            'minute_remaining': minute_limit - minute_requests,
            'hour_remaining': hour_limit - hour_requests
        }
    
    def reset_user_limits(self, user_id):
        """Reset rate limits for a specific user (admin function)"""
        self.user_requests[user_id] = []
        logger.info(f"Rate limits reset for user {user_id}")
    
    def get_global_stats(self):
        """Get global usage statistics"""
        current_time = time.time()
        
        total_users = len(self.user_requests)
        premium_users = len(self.premium_users)
        
        # Count active users (made request in last hour)
        hour_ago = current_time - 3600
        active_users = 0
        total_requests_hour = 0
        
        for user_id, requests in self.user_requests.items():
            user_hour_requests = [req for req in requests if req > hour_ago]
            if user_hour_requests:
                active_users += 1
                total_requests_hour += len(user_hour_requests)
        
        return {
            'total_users': total_users,
            'premium_users': premium_users,
            'active_users_hour': active_users,
            'total_requests_hour': total_requests_hour
        }
