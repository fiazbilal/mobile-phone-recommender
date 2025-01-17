# File: data_cleaner.py
import re
import pandas as pd

def clean_mobile_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess mobile phone data
    
    Args:
        raw_data: DataFrame with raw mobile phone data
        
    Returns:
        Cleaned DataFrame
    """
    df = raw_data.copy()
    
    # Clean price - remove currency symbols and convert to numeric
    df['Prices'] = df['Prices'].apply(lambda x: float(''.join(re.findall(r'\d+', str(x)))))
    
    # Clean processor names
    df['Processor'] = df['Processor'].apply(lambda x: x.replace(' Processor', '').strip())
    
    # Ensure RAM is numeric
    df['RAM'] = pd.to_numeric(df['RAM'], errors='coerce')
    
    # Clean brand names
    df['Brand'] = df['Brand'].str.upper()
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['Model', 'Prices', 'RAM'])
    
    return df