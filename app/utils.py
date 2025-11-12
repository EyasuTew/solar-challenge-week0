import pandas as pd
import numpy as np
from scipy import stats
import os

def load_data(country):
    file_map = {
        'Benin': '../data/benin_clean.csv',
        'Sierra Leone': '../data/sierraleone_clean.csv',
        'Togo': '../data/togo_clean.csv'
    }
    filename = file_map.get(country)
    filepath = os.path.join('data', filename)
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, parse_dates=['Timestamp'])
        df.set_index('Timestamp', inplace=True)
        return df
    # Fallback for no-data runs
    timestamps = pd.date_range('2021-01-01', periods=1000, freq='H')
    np.random.seed(42)
    return pd.DataFrame({
        'GHI': np.random.normal(0, 1, 1000), 'DNI': np.random.normal(0, 0.5, 1000), 'DHI': np.random.normal(0, 0.8, 1000),
        'RH': np.random.uniform(70, 100, 1000), 'Tamb': np.random.normal(25, 5, 1000)
    }, index=timestamps)

def clean_data(df):
    key_cols = ['GHI', 'DNI', 'DHI']
    if all(col in df for col in key_cols):
        z_scores = df[key_cols].apply(stats.zscore)
        df['outlier_flag'] = (np.abs(z_scores) > 3).any(axis=1)
        for col in key_cols:
            df.loc[df['outlier_flag'], col] = df[col].median()
    return df

def get_summary_stats(df):
    return df[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)

def rank_countries():
    countries = ['Benin', 'Sierra Leone', 'Togo']
    rankings = {c: load_data(c)['GHI'].mean() for c in countries}
    return pd.DataFrame(list(rankings.items()), columns=['Country', 'Avg GHI']).sort_values('Avg GHI', ascending=False)