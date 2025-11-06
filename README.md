# Solar Challenge Week 0

## Setup Instructions
1. Clone the repo: `git clone https://github.com/EyasuTew/solar-challenge-week0.git`
2. Linux: Create & activate venv: `python -m venv .venv && source .venv/bin/activate`
2. Windows: Create & activate venv: `python -m venv .venv && .\.venv\Scripts\activate.bat`
3. Install deps: `pip install -r requirements.txt`
4. (For data tasks) Place cleaned CSVs in `data/` (ignored in Git).
5. Run notebooks: `jupyter notebook notebooks/`

## Folder Structure
- `src/`: Core Python modules.
- `notebooks/`: EDA and analysis Jupyter notebooks.
- `tests/`: Unit tests.
- `scripts/`: Utility scripts.
- `app/`: Streamlit dashboard (bonus).

## Development
- Branch from `main` for features (e.g., `git checkout -b eda-benin`).
- Use PRs for merges.