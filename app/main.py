# Main Streamlit app: Widgets, GHI boxplot, top regions table
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from app.utils import load_data, clean_data, get_summary_stats, rank_countries

st.set_page_config(page_title="Solar Dashboard", layout="wide", initial_sidebar_state="expanded")
sns.set_style("whitegrid")

st.title("🌞 Solar Challenge Interactive Dashboard")
st.markdown("Select a country below to explore GHI distributions and rankings. Filters update dynamically.")

# Sidebar: Widgets for usability
st.sidebar.header("Controls")
country = st.sidebar.selectbox("Select Country", ['Benin', 'Sierra Leone', 'Togo'])
rh_max = st.sidebar.slider("Max RH (%)", 70, 100, 95)
apply_clean = st.sidebar.checkbox("Apply Cleaning", value=True)

# Dynamic processing
@st.cache_data
def process_data(country, rh_max, apply_clean):
    df = load_data(country)
    if apply_clean:
        df = clean_data(df)
    df_filtered = df[df['RH'] <= rh_max] if 'RH' in df.columns else df
    return df_filtered

df = process_data(country, rh_max, apply_clean)

# Main content
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Summary Stats")
    if not df.empty:
        summary = get_summary_stats(df)
        st.dataframe(summary, use_container_width=True)

with col2:
    st.subheader(f"📈 GHI Boxplot - {country}")
    if not df.empty and 'GHI' in df.columns:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(y='GHI', data=df, ax=ax, color='gold')
        ax.set_title(f"GHI Distribution (Filtered RH ≤ {rh_max}%)")
        st.pyplot(fig)

# Top regions table (interactive button for engagement)
if st.sidebar.button("Show Top Regions Ranking"):
    st.subheader("🏆 Top Regions by Avg GHI")
    rank_df = rank_countries()
    st.table(rank_df)

# Additional appeal: Insights
st.markdown("---")
st.info("**Insight**: Higher avg GHI indicates better solar potential. Use filters to simulate conditions.")