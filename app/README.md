# Solar Insights Project

## Interactive Dashboard
- **App**: Run `streamlit run app/main.py` locally.
- **Features**:
  - Upload CSV for custom solar data (e.g., GHI, RH).
  - Filter by RH max and clean outliers.
  - View summary stats, GHI boxplot, and top regions (button-triggered).
  - Fallback: Simulated hourly data (2021).
- **Deployment**: https://eyasu-dashboard-dev.streamlit.app/
- **Usage**: Adjust sidebar; upload encouraged for real insights. Higher GHI = better solar potential!
- **Tech**: Streamlit, Pandas, Seaborn. No external data—code-only.

## Development Notes
- Branch: dashboard-dev.
- Utils: clean_data (IQR outliers), get_summary_stats (describe()).
- Future: Integrate real country rankings via rank_countries().