import hashlib
import json
import time
from typing import Optional, Dict, Any
from logger import get_logger

logger = get_logger(__name__)

class ResponseCache:
    """Cache system to reduce OpenAI API calls for similar queries"""
    
    def __init__(self, cache_ttl: int = 3600):  # 1 hour default TTL
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.cache_ttl = cache_ttl
        
    def _generate_cache_key(self, prompt: str, command_type: str = "general") -> str:
        """Generate a cache key for the prompt"""
        # Normalize the prompt by removing extra spaces and converting to lowercase
        normalized_prompt = " ".join(prompt.lower().strip().split())
        cache_string = f"{command_type}:{normalized_prompt}"
        return hashlib.md5(cache_string.encode()).hexdigest()
    
    def get_cached_response(self, prompt: str, command_type: str = "general") -> Optional[str]:
        """Get cached response if available and not expired"""
        cache_key = self._generate_cache_key(prompt, command_type)
        
        if cache_key in self.cache:
            cache_entry = self.cache[cache_key]
            current_time = time.time()
            
            # Check if cache entry is still valid
            if current_time - cache_entry['timestamp'] < self.cache_ttl:
                logger.info(f"Cache hit for prompt: {prompt[:50]}...")
                return cache_entry['response']
            else:
                # Remove expired entry
                del self.cache[cache_key]
                logger.info(f"Cache expired for prompt: {prompt[:50]}...")
        
        return None
    
    def cache_response(self, prompt: str, response: str, command_type: str = "general"):
        """Cache a response"""
        cache_key = self._generate_cache_key(prompt, command_type)
        self.cache[cache_key] = {
            'response': response,
            'timestamp': time.time(),
            'command_type': command_type
        }
        logger.info(f"Cached response for prompt: {prompt[:50]}...")
    
    def clear_expired_entries(self):
        """Remove expired cache entries"""
        current_time = time.time()
        expired_keys = []
        
        for key, entry in self.cache.items():
            if current_time - entry['timestamp'] >= self.cache_ttl:
                expired_keys.append(key)
        
        for key in expired_keys:
            del self.cache[key]
        
        if expired_keys:
            logger.info(f"Cleared {len(expired_keys)} expired cache entries")
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        current_time = time.time()
        valid_entries = 0
        expired_entries = 0
        
        for entry in self.cache.values():
            if current_time - entry['timestamp'] < self.cache_ttl:
                valid_entries += 1
            else:
                expired_entries += 1
        
        return {
            'total_entries': len(self.cache),
            'valid_entries': valid_entries,
            'expired_entries': expired_entries,
            'cache_ttl_hours': self.cache_ttl / 3600
        }
    
    def clear_cache(self):
        """Clear all cache entries"""
        self.cache.clear()
        logger.info("Cache cleared")

# Global cache instance
response_cache = ResponseCache()