# File: price_analyzer.py
def analyze_price_ranges(phones_df: pd.DataFrame) -> dict:
    """
    Analyze price distribution and create price ranges
    
    Args:
        phones_df: DataFrame with phone data
        
    Returns:
        Dictionary with price range analysis
    """
    price_stats = {
        'budget': {
            'range': (0, 15000),
            'phones': len(phones_df[phones_df['Prices'] <= 15000]),
            'avg_rating': phones_df[phones_df['Prices'] <= 15000]['Ratings'].mean()
        },
        'mid_range': {
            'range': (15001, 25000),
            'phones': len(phones_df[(phones_df['Prices'] > 15000) & (phones_df['Prices'] <= 25000)]),
            'avg_rating': phones_df[(phones_df['Prices'] > 15000) & (phones_df['Prices'] <= 25000)]['Ratings'].mean()
        },
        'premium': {
            'range': (25001, float('inf')),
            'phones': len(phones_df[phones_df['Prices'] > 25000]),
            'avg_rating': phones_df[phones_df['Prices'] > 25000]['Ratings'].mean()
        }
    }
    
    return price_stats