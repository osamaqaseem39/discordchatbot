import json
import os
import asyncio
from openai import OpenAI
from config import OPENAI_CONFIG, CACHE_CONFIG
from response_cache import response_cache
from logger import get_logger

logger = get_logger(__name__)

class OpenAIService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            logger.error("OPENAI_API_KEY not found in environment variables")
            raise ValueError("OpenAI API key is required")
        
        self.client = OpenAI(api_key=self.api_key)
        
    async def get_educational_response(self, prompt, command_type="general"):
        """Get educational response from OpenAI with caching and Amazon FBA context"""
        try:
            # Check cache first if enabled
            if CACHE_CONFIG['enabled']:
                cached_response = response_cache.get_cached_response(prompt, command_type)
                if cached_response:
                    logger.info("Returning cached response - API call saved!")
                    return cached_response
            
            # Run the synchronous OpenAI call in a thread pool
            response = await asyncio.get_event_loop().run_in_executor(
                None, self._make_openai_request, prompt
            )
            
            # Cache the response if caching is enabled and response is valid
            if CACHE_CONFIG['enabled'] and response:
                response_cache.cache_response(prompt, response, command_type)
            
            return response
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise Exception(f"Unable to generate response: {str(e)}")
    
    def _make_openai_request(self, prompt):
        """Make synchronous OpenAI API request"""
        try:
            response = self.client.chat.completions.create(
                model=OPENAI_CONFIG['model'],  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024. do not change this unless explicitly requested by the user
                messages=[
                    {
                        "role": "system",
                        "content": OPENAI_CONFIG['system_prompt']
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=OPENAI_CONFIG['max_tokens'],
                temperature=OPENAI_CONFIG['temperature']
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error in OpenAI request: {e}")
            raise
    
    async def analyze_profit_scenario(self, selling_price, cost, additional_costs=None):
        """Specialized method for profit analysis with structured output"""
        try:
            prompt = f"""
            Analyze this Amazon FBA profit scenario and respond with detailed calculations:
            - Selling Price: ${selling_price}
            - Product Cost: ${cost}
            - Additional Costs: {additional_costs or 'Standard FBA costs'}
            
            Please provide:
            1. Detailed fee breakdown
            2. Net profit calculation
            3. Profit margin percentage
            4. ROI analysis
            5. Recommendations for optimization
            
            Format the response as clear, actionable information for an Amazon FBA seller.
            """
            
            response = await asyncio.get_event_loop().run_in_executor(
                None, self._make_structured_request, prompt
            )
            return response
        except Exception as e:
            logger.error(f"Error in profit analysis: {e}")
            raise
    
    def _make_structured_request(self, prompt):
        """Make structured OpenAI request for financial analysis"""
        try:
            response = self.client.chat.completions.create(
                model=OPENAI_CONFIG['model'],  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024. do not change this unless explicitly requested by the user
                messages=[
                    {
                        "role": "system",
                        "content": OPENAI_CONFIG['system_prompt'] + "\n\nProvide structured, detailed financial analysis with specific numbers and actionable recommendations."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=OPENAI_CONFIG['max_tokens'],
                temperature=0.3  # Lower temperature for more precise calculations
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error in structured request: {e}")
            raise
    
    async def get_market_analysis(self, niche, analysis_type="comprehensive"):
        """Get market analysis for specific niches"""
        try:
            prompt = f"""
            Provide a {analysis_type} Amazon FBA market analysis for the '{niche}' niche.
            
            Include:
            1. Market size and demand indicators
            2. Competition level assessment
            3. Average profit margins
            4. Seasonal trends and patterns
            5. Top product opportunities
            6. Entry barriers and challenges
            7. Marketing and differentiation strategies
            8. Risk factors and mitigation
            
            Provide specific, actionable insights based on current market conditions.
            """
            
            response = await asyncio.get_event_loop().run_in_executor(
                None, self._make_openai_request, prompt
            )
            return response
        except Exception as e:
            logger.error(f"Error in market analysis: {e}")
            raise
    
    async def generate_product_launch_plan(self, product_info):
        """Generate comprehensive product launch plan"""
        try:
            prompt = f"""
            Create a detailed Amazon FBA product launch plan for: {product_info}
            
            Include:
            1. Pre-launch preparation (timeline: weeks -8 to -1)
            2. Launch week strategy
            3. Post-launch optimization (weeks 1-12)
            4. Budget allocation recommendations
            5. Key performance indicators to track
            6. Risk management strategies
            7. Scaling opportunities
            
            Provide a week-by-week action plan with specific tasks and milestones.
            """
            
            response = await asyncio.get_event_loop().run_in_executor(
                None, self._make_openai_request, prompt
            )
            return response
        except Exception as e:
            logger.error(f"Error generating launch plan: {e}")
            raise
    
    async def health_check(self):
        """Test OpenAI API connectivity"""
        try:
            response = await asyncio.get_event_loop().run_in_executor(
                None, lambda: self.client.chat.completions.create(
                    model=OPENAI_CONFIG['model'],  # the newest OpenAI model is "gpt-4o" which was released May 13, 2024. do not change this unless explicitly requested by the user
                    messages=[{"role": "user", "content": "Test connection"}],
                    max_tokens=10
                )
            )
            return True
        except Exception as e:
            logger.error(f"OpenAI health check failed: {e}")
            return False
