# Solar Challenge Week 0

## Setup
1. `git clone https://github.com/yourusername/solar-challenge-week0.git`
2. `python -m venv .venv && source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `jupyter notebook notebooks/` for EDA
5. `streamlit run app/main.py` for dashboard

## Structure
- `notebooks/`: EDA per country + comparison
- `app/`: Streamlit dashboard
- `scripts/`: Utils + deployment guide
- `data/`: Local CSVs (ignored)

Deploy dashboard: See scripts/README.md