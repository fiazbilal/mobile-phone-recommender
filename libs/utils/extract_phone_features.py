# File: feature_extractor.py
def extract_phone_features(model_name: str) -> dict:
    """
    Extract features from phone model name
    
    Args:
        model_name: Full model name of the phone
        
    Returns:
        Dictionary of extracted features
    """
    features = {}
    
    # Extract brand
    brand_match = re.match(r'^([A-Za-z]+)', model_name)
    if brand_match:
        features['brand'] = brand_match.group(1)
    
    # Extract storage capacity
    storage_match = re.search(r'(\d+)\s*GB', model_name)
    if storage_match:
        features['storage'] = int(storage_match.group(1))
    
    # Extract color
    color_match = re.search(r'\((.*?)[,\)]', model_name)
    if color_match:
        features['color'] = color_match.group(1)
    
    # Extract if 5G
    features['is_5g'] = '5G' in model_name
    
    # Extract model number/name
    model_number = re.search(r'([A-Za-z0-9]+\s*[0-9]+)', model_name)
    if model_number:
        features['model_number'] = model_number.group(1)
    
    return features