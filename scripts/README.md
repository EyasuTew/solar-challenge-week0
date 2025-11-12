# Dashboard Development & Usage

## Development Process
1. Branched `dashboard-dev` from `main`.
2. Implemented `utils.py` for CSV loading/cleaning (dynamic, no data commit).
3. Built `main.py`: Country dropdown, RH slider, cleaning checkbox, GHI boxplot, ranking button/table.
4. Styled for appeal: Icons, wide layout, cached processing.
5. Tested locally: `streamlit run app/main.py` – Widgets update plots/tables.
6. Committed: "feat: basic Streamlit UI with country widgets, GHI boxplot, and rankings table".
7. PR to `main`: Reviewed for KPIs (usability: labels/help; interactive: widgets; appeal: colors/grids; success: functional).

## Usage Instructions
- Local: Activate venv, `streamlit run app/main.py` → http://localhost:8501.
- Place CSVs in `data/` (e.g., benin_clean.csv).
- Deploy: See below.

## Deployment to Streamlit Cloud
1. Push to GitHub `main`.
2. [share.streamlit.io](https://share.streamlit.io) → New app → Repo: solar-challenge-week0 → File: app/main.py → Deploy.
3. URL: https://solar-challenge-week0.streamlit.app (customize name).
4. For data: Upload CSVs via Git LFS or secrets (app settings).

KPIs: Sidebar intuitive, widgets engaging (e.g., button reveals table), clean design communicates GHI insights, deployed & public.