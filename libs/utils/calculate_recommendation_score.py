def calculate_recommendation_score(phone_specs: dict, user_preferences: dict) -> float:
    """
    Calculate recommendation score based on user preferences
    
    Args:
        phone_specs: Phone specifications
        user_preferences: User's feature preferences and weights
        
    Returns:
        Recommendation score between 0 and 1
    """
    score = 0
    total_weight = sum(user_preferences.values())
    
    # Score for price (lower is better)
    if 'price_weight' in user_preferences:
        max_price = 40000  # Maximum price threshold
        price_score = 1 - (phone_specs['Prices'] / max_price)
        score += (price_score * user_preferences['price_weight'])
    
    # Score for RAM (higher is better)
    if 'ram_weight' in user_preferences:
        ram_score = phone_specs['RAM'] / 8  # Normalize to 8GB
        score += (ram_score * user_preferences['ram_weight'])
    
    # Score for battery (higher is better)
    if 'battery_weight' in user_preferences:
        battery_score = phone_specs['Battery'] / 6000  # Normalize to 6000mAh
        score += (battery_score * user_preferences['battery_weight'])
    
    # Score for ratings
    if 'rating_weight' in user_preferences:
        rating_score = phone_specs['Ratings'] / 5  # Normalize to 5 stars
        score += (rating_score * user_preferences['rating_weight'])
    
    return round(score / total_weight, 2)
