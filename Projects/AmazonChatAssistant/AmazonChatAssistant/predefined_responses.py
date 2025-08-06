"""
Predefined responses for common Amazon FBA questions to reduce API usage
"""

PREDEFINED_RESPONSES = {
    "general_research": {
        "title": "🔍 Amazon FBA Product Research Basics",
        "content": """**Essential Product Research Strategies:**

**1. Market Validation Tools**
• Jungle Scout - Market size analysis
• Helium 10 - Keyword research & competition
• AMZScout - Product database search
• Keepa - Price history tracking

**2. Key Metrics to Analyze**
• Monthly search volume: 3,000+ searches
• Competition level: <100 reviews for top 3
• Price range: $15-50 optimal sweet spot
• Profit margin: Minimum 30-40%

**3. Product Criteria Checklist**
✓ Lightweight (<2 lbs for shipping)
✓ Small/medium size (easy storage)
✓ Durable (avoid fragile items)
✓ Year-round demand
✓ Room for improvement over competitors

**4. Red Flags to Avoid**
• Seasonal products only
• High competition (>500 reviews top 3)
• Legal/safety restrictions
• Fragile or hazardous items
• Brand dominated categories"""
    },
    
    "amazon_fees": {
        "title": "📋 Amazon FBA Fee Structure 2024",
        "content": """**Amazon FBA Fee Breakdown:**

**1. Referral Fees (8-15% of selling price)**
• Most categories: 8-15%
• Electronics: 8%
• Toys & Games: 15%
• Books: 15%

**2. FBA Fulfillment Fees**
• Small standard: $3.22 + $0.50/lb
• Large standard: $4.09 + $0.50/lb
• Oversized: $9.61 + $0.50/lb

**3. Storage Fees (Monthly)**
• Jan-Sep: $0.87/cubic foot
• Oct-Dec: $2.40/cubic foot
• Long-term (365+ days): +$6.90/cubic foot

**4. Additional Fees**
• Removal fees: $0.50-$0.60 per unit
• Return processing: $2.50-$5.00
• Prep fees: $0.50-$1.30 per unit

**Calculator Formula:**
Revenue - (Referral Fee + FBA Fee + Storage + COGS) = Net Profit"""
    },
    
    "profit_basics": {
        "title": "💰 Amazon FBA Profit Calculation Guide",
        "content": """**Basic Profit Formula:**

**Revenue Calculation:**
Selling Price × Units Sold = Gross Revenue

**Cost Breakdown:**
• Product Cost (COGS): 25-40% of selling price
• Amazon Fees: 20-25% of selling price
• Shipping to Amazon: $0.50-$2.00 per unit
• PPC Advertising: 10-20% of revenue
• Miscellaneous: 3-5% of revenue

**Example Calculation ($25 Product):**
• Selling Price: $25.00
• Amazon Fees (25%): -$6.25
• Product Cost: -$8.00
• Shipping: -$1.50
• PPC (15%): -$3.75
• **Net Profit: $5.50 (22% margin)**

**Target Margins:**
• Beginner: 20-25%
• Experienced: 25-35%
• Premium brands: 35-50%

**ROI Calculation:**
(Net Profit ÷ Total Investment) × 100 = ROI%"""
    },
    
    "launch_strategy": {
        "title": "🚀 Amazon FBA Product Launch Framework",
        "content": """**Pre-Launch Phase (8 weeks):**

**Weeks 1-2: Setup**
• Create Amazon Seller account
• Set up business structure & tax ID
• Order initial inventory (500-1000 units)
• Design packaging & labels

**Weeks 3-4: Listing Optimization**
• Professional product photography
• Keyword research & listing copy
• A+ Content creation
• Brand registration

**Weeks 5-6: Inventory & Logistics**
• Ship inventory to Amazon FBA
• Set up inventory monitoring
• Create shipping plans

**Weeks 7-8: Marketing Preparation**
• Set up PPC campaigns
• Create promotional strategy
• Build email list
• Social media setup

**Launch Week Strategy:**
• Start with lower price for reviews
• Run aggressive PPC campaigns
• Give away 10-20 units for reviews
• Monitor BSR and adjust pricing

**Post-Launch (Weeks 1-12):**
• Optimize PPC campaigns
• Gather customer feedback
• Improve listing based on data
• Scale advertising budget"""
    }
}

def get_predefined_response(key):
    """Get a predefined response if available"""
    return PREDEFINED_RESPONSES.get(key, None)

def search_predefined_responses(query):
    """Search for relevant predefined responses based on query"""
    query_lower = query.lower()
    
    # Map keywords to response keys
    keyword_mapping = {
        'research': ['general_research'],
        'product research': ['general_research'],
        'how to research': ['general_research'],
        'fees': ['amazon_fees'],
        'amazon fees': ['amazon_fees'],
        'fba fees': ['amazon_fees'],
        'cost': ['amazon_fees'],
        'profit': ['profit_basics'],
        'profit calculation': ['profit_basics'],
        'margin': ['profit_basics'],
        'roi': ['profit_basics'],
        'launch': ['launch_strategy'],
        'product launch': ['launch_strategy'],
        'launching': ['launch_strategy'],
        'how to launch': ['launch_strategy']
    }
    
    for keyword, response_keys in keyword_mapping.items():
        if keyword in query_lower:
            return response_keys[0]
    
    return None