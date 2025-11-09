import pandas as pd
from typing import Optional

def load_benin_data(file_path: str, timestamp_col: str = 'Timestamp') -> pd.DataFrame:
    """
    Load the Benin-Malanville CSV and prepare the DataFrame.
    
    Args:
        file_path: Path to CSV.
        timestamp_col: Name of timestamp column.
    
    Returns:
        DataFrame with timestamp index.
    """
    df = pd.read_csv(file_path, parse_dates=[timestamp_col])
    df.set_index(timestamp_col, inplace=True)
    
    # Drop fully missing columns (e.g., Comments)
    df.dropna(axis=1, how='all', inplace=True)
    
    return df

def handle_missing(df: pd.DataFrame, method: str = 'drop') -> pd.DataFrame:
    """
    Handle missing values (your report shows mostly none, but future-proof).
    
    Args:
        df: Input DataFrame.
        method: 'drop' or 'ffill' (forward fill).
    
    Returns:
        Cleaned DataFrame.
    """
    if method == 'drop':
        return df.dropna()
    elif method == 'ffill':
        return df.ffill()
    else:
        raise ValueError("Method must be 'drop' or 'ffill'")