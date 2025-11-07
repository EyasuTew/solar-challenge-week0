# Utility functions: Dynamic CSV loading, cleaning, stats
import pandas as pd
import numpy as np
from scipy import stats
import os

def load_data(country):
    """
    Fetch cleaned CSV dynamically from data/ (local; no commit).
    Assumes files: data/benin_clean.csv, data/sierraleone_clean.csv, data/togo_clean.csv
    """
    file_map = {
        'Benin': 'benin_clean.csv',
        'Sierra Leone': 'sierraleone_clean.csv',
        'Togo': 'togo_clean.csv'
    }
    filename = file_map.get(country)
    filepath = os.path.join('data', filename)
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, parse_dates=['Timestamp'])
        df.set_index('Timestamp', inplace=True)
        return df
    else:
        # Fallback simulated data for testing (remove in prod)
        print(f"Warning: {filepath} not found; using simulated data")
        timestamps = pd.date_range(start='2021-01-01', periods=1000, freq='H')
        np.random.seed(42)  # Reproducible
        return pd.DataFrame({
            'GHI': np.random.normal(0, 1, 1000),
            'DNI': np.random.normal(0, 0.5, 1000),
            'DHI': np.random.normal(0, 0.8, 1000),
            'Tamb': np.random.normal(25, 5, 1000),
            'RH': np.random.uniform(70, 100, 1000),
            'WS': np.random.uniform(0, 5, 1000),
            'WD': np.random.uniform(0, 360, 1000),
            'ModA': np.random.uniform(0, 10, 1000),
            'ModB': np.random.uniform(0, 10, 1000)
        }, index=timestamps)

def clean_data(df):
    """Z-score outlier flagging and median imputation."""
    key_cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS']
    if all(col in df.columns for col in key_cols):
        z_scores = df[key_cols].apply(stats.zscore, nan_policy='omit')
        df['outlier_flag'] = (np.abs(z_scores) > 3).any(axis=1)
        for col in key_cols:
            median_val = df[col].median()
            df.loc[df['outlier_flag'], col] = median_val
    return df

def get_summary_stats(df):
    """Table for top regions (GHI metrics)."""
    metrics = ['GHI', 'DNI', 'DHI']
    return df[metrics].agg(['mean', 'median', 'std']).round(2)

def rank_countries():
    """Mock top regions table (load all for ranking)."""
    countries = ['Benin', 'Sierra Leone', 'Togo']
    rankings = {}
    for c in countries:
        df_c = load_data(c)
        df_c = clean_data(df_c)
        rankings[c] = df_c['GHI'].mean()
    rank_df = pd.DataFrame(list(rankings.items()), columns=['Country', 'Avg GHI']).sort_values('Avg GHI', ascending=False)
    return rank_df