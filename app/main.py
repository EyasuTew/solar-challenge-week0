import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils import load_data, clean_data, get_summary_stats, rank_countries

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
sns.set_style("whitegrid")

st.title("🌞 Solar Insights Dashboard")
st.markdown("**Explore solar data interactively.** Select country, filter RH, and view GHI distributions/rankings.")

st.sidebar.header("🛠️ Controls")
country = st.sidebar.selectbox("Country", ['Benin', 'Sierra Leone', 'Togo'])
rh_max = st.sidebar.slider("Max RH (%)", 70.0, 100.0, 95.0)
cleaning = st.sidebar.checkbox("Apply Outlier Cleaning")

@st.cache_data
def process_df(country, rh_max, cleaning):
    df = load_data(country)
    if cleaning:
        df = clean_data(df)
    return df[df['RH'] <= rh_max] if 'RH' in df else df

df = process_df(country, rh_max, cleaning)

col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("📊 Stats")
    if not df.empty:
        st.dataframe(get_summary_stats(df))
with col2:
    st.subheader("📈 GHI Boxplot")
    if not df.empty:
        fig, ax = plt.subplots()
        sns.boxplot(y='GHI', data=df, ax=ax, color='orange')
        ax.set_title(f"GHI - {country} (RH ≤ {rh_max}%)")
        st.pyplot(fig)

if st.sidebar.button("🏆 Show Top Regions"):
    st.subheader("Top Regions Table")
    st.table(rank_countries())

st.info("**Tip**: Higher GHI = better solar potential. Ranking updates on load.")