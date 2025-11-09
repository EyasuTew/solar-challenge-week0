#!/usr/bin/env python
# Run as: python scripts/run_eda.py

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from src.data_loader import load_benin_data, handle_missing
from src.analytics.stats import SummaryStats
from src.analytics.outliers import detect_outliers_zscore, get_outlier_summary
from src.analytics.correlations import compute_correlations, plot_correlations, bubble_plot
from src.utils.plotter import plot_distributions

# Config
DATA_PATH = '../data/benin-malanville.csv'
KEY_COLS = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust', 'Tamb', 'RH']
OUTLIER_COLS = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']

# Pipeline
df = load_benin_data(DATA_PATH)
df = handle_missing(df)  # If needed

# Stats
stats_analyzer = SummaryStats(df)
print(stats_analyzer.compute_stats(KEY_COLS))
print(stats_analyzer.missing_report())

# Outliers
df_out = detect_outliers_zscore(df, OUTLIER_COLS)
summary = get_outlier_summary(df_out)
print(f"Outliers: {summary}")
df_out[df_out['outlier_flag']].to_csv('../outputs/outlier_report.csv')

# Correlations
corr = compute_correlations(df, KEY_COLS)
plot_correlations(corr)
bubble_plot(df, 'GHI', 'Tamb', 'RH')

# Distributions
plot_distributions(df, KEY_COLS)

# Save stats
stats_analyzer.compute_stats(KEY_COLS).to_csv('../outputs/stats_summary.csv')
print("EDA complete. Outputs saved.")