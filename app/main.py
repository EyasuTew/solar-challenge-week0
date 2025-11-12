# app/main.py
# Main Streamlit app: Now with CSV upload for custom data analysis
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np  # For simulated fallback
from utils import clean_data, get_summary_stats

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
sns.set_style("whitegrid")

st.title("🌞 Solar Insights Dashboard")
st.markdown("**Explore solar data interactively.**"+ 
            " Upload your CSV to analyze GHI "+ 
            "distributions and rankings. "+ 
            "(No upload? Use simulated sample data.)")

# Sidebar: Controls + Upload Widget (Primary Focus)
st.sidebar.header("🛠️ Controls")
uploaded_file = st.sidebar.file_uploader(
    "📁 Upload CSV Data",
    type=['csv'],
    help="Upload a CSV with columns like "+ 
    "Timestamp, GHI, DNI, DHI, RH. Analyzes immediately!"
)

rh_max = st.sidebar.slider("Max RH (%)", 70.0, 100.0, 95.0)
cleaning = st.sidebar.checkbox("Apply Outlier Cleaning")


@st.cache_data
def process_df(df_input, rh_max, cleaning):
    """Process DF (from upload or simulated): Clean and filter."""
    if cleaning:
        df_input = clean_data(df_input)
    if 'RH' in df_input.columns:
        df_input = df_input[df_input['RH'] <= rh_max]
    return df_input


# Load/Process Data Dynamically
if uploaded_file is not None:
    # Upload Mode: Read and process uploaded CSV
    df = pd.read_csv(uploaded_file, parse_dates=['Timestamp'])
    if 'Timestamp' in df.columns:
        df.set_index('Timestamp', inplace=True)
    df = process_df(df, rh_max, cleaning)
    data_source = "Uploaded CSV"
else:
    # Fallback: Simulated Data
    timestamps = pd.date_range('2021-01-01',
                               periods=1000,
                               freq='h')
    np.random.seed(42)
    df = pd.DataFrame({
        'GHI': np.random.normal(0, 1, 1000),
        'DNI': np.random.normal(0, 0.5, 1000),
        'DHI': np.random.normal(0, 0.8, 1000),
        'RH': np.random.uniform(70, 100, 1000),
        'Tamb': np.random.normal(25, 5, 1000),
        'ModA': np.random.uniform(0, 10, 1000),
        'ModB': np.random.uniform(0, 10, 1000)
    }, index=timestamps)
    df = process_df(df, rh_max, cleaning)
    data_source = "Simulated Sample Data"

if df.empty:
    st.warning("No data after filtering. "+ 
               "Adjust controls or upload valid CSV.")
    st.stop()

# Main Layout: Stats and Plot
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("📊 Summary Stats")
    summary = get_summary_stats(df)
    st.dataframe(summary, use_container_width=True)
    st.caption(f"Source: {data_source} | Rows: {len(df)}")

with col2:
    st.subheader("📈 GHI Boxplot")
    if 'GHI' in df.columns:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(y='GHI', data=df, ax=ax, color='orange')
        ax.set_title(
            f"GHI Distribution - {data_source} (RH ≤ {rh_max}%)")
        st.pyplot(fig)
    else:
        st.warning("No 'GHI' column found. Check CSV headers.")

# Top Regions Table (Mock)
if st.sidebar.button("🏆 Show Top Regions"):
    st.subheader("🏆 Top Regions Ranking (Avg GHI)")
    # Mock ranking for fallback
    mock_rank = pd.DataFrame({
        'Country': ['Sample Region 1',
                     'Sample Region 2',
                     'Sample Region 3'],
        'Avg GHI': [0.5, 0.2, -0.1]
    }).sort_values('Avg GHI', ascending = False)
    if uploaded_file is not None:
        custom_avg = df['GHI'].mean() if 'GHI' in df else np.nan
        custom_row = pd.DataFrame([['Custom Upload', custom_avg]],
                                  columns=['Country', 'Avg GHI'])
        mock_rank = pd.concat(
            [mock_rank, custom_row],
            ignore_index=True).sort_values('Avg GHI', ascending=False)
    st.table(mock_rank)

st.info("**Tip**: Higher GHI = better solar potential."+ 
        " Upload your CSV to analyze custom data—e.g., from EDA notebooks!")
