import numpy as np
import pandas as pd
from scipy import stats
from typing import List

def detect_outliers_zscore(df: pd.DataFrame, columns: List[str], threshold: float = 3.0) -> pd.DataFrame:
    """
    Detect outliers using Z-score (|Z| > threshold).
    
    Step-by-step:
    1. Compute Z = (x - μ) / σ for each column (vectorized via scipy.stats.zscore).
    2. Flag rows where any |Z| > threshold (e.g., 3 for ~0.3% tails assuming normality).
    3. Handle NaN/zero-std (e.g., ModA=0 → Z=NaN, skipped via nan_policy='omit').
    
    Args:
        df: Input DataFrame.
        columns: List of columns to check (e.g., ['GHI', 'DNI', ...]).
        threshold: Z-score cutoff.
    
    Returns:
        DataFrame with 'outlier_flag' column (True if outlier).
    """
    key_cols = df[columns]
    z_scores = key_cols.apply(stats.zscore, nan_policy='omit')
    outlier_flags = (np.abs(z_scores) > threshold).any(axis=1)
    df_out = df.copy()
    df_out['outlier_flag'] = outlier_flags
    return df_out

def get_outlier_summary(df_out: pd.DataFrame) -> dict:
    """Summary: count, % outliers."""
    n_outliers = df_out['outlier_flag'].sum()
    pct = (n_outliers / len(df_out)) * 100
    return {'outlier_count': n_outliers, 'outlier_pct': pct}