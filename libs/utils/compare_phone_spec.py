def compare_phone_specs(phone1_specs: dict, phone2_specs: dict) -> dict:
    """
    Compare specifications of two phones
    
    Args:
        phone1_specs: Specifications of first phone
        phone2_specs: Specifications of second phone
        
    Returns:
        Dictionary with comparison results
    """
    comparison = {}
    
    # Compare prices
    price_diff = abs(phone1_specs['Prices'] - phone2_specs['Prices'])
    comparison['price_difference'] = price_diff
    
    # Compare RAM
    ram_diff = phone2_specs['RAM'] - phone1_specs['RAM']
    comparison['ram_difference'] = ram_diff
    
    # Compare battery
    battery_diff = phone2_specs['Battery'] - phone1_specs['Battery']
    comparison['battery_difference'] = battery_diff
    
    # Compare processors
    comparison['same_processor'] = phone1_specs['Processor'] == phone2_specs['Processor']
    
    # Overall value comparison
    comparison['better_value'] = 'Phone 1' if (phone1_specs['Ratings'] / phone1_specs['Prices']) > (phone2_specs['Ratings'] / phone2_specs['Prices']) else 'Phone 2'
    
    return comparison
