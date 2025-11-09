import pandas as pd
from typing import List, Optional

class SummaryStats:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def compute_stats(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """Compute describe() on selected columns."""
        if columns:
            return self.df[columns].describe()
        return self.df.describe()
    
    def missing_report(self) -> pd.DataFrame:
        """Missing count and %."""
        missing_count = self.df.isnull().sum()
        missing_pct = (missing_count / len(self.df)) * 100
        report = pd.DataFrame({
            'Missing Count': missing_count,
            'Missing %': missing_pct
        })
        # Filter to show only >0% (as in your notebook)
        return report[report['Missing %'] > 0] if not report.empty else report