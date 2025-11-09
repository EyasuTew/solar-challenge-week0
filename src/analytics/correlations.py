import matplotlib.pyplot as plt
import seaborn as sns
from typing import List

def compute_correlations(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Pearson correlation matrix for selected columns."""
    return df[columns].corr()

def plot_correlations(corr_matrix: pd.DataFrame, figsize: tuple = (10, 8)):
    """Heatmap of correlations."""
    plt.figure(figsize=figsize)
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.show()

def bubble_plot(df: pd.DataFrame, x_col: str, y_col: str, size_col: str):
    """Your bubble chart: GHI vs Tamb, size=RH."""
    sns.scatterplot(data=df, x=x_col, y=y_col, size=size_col, sizes=(20, 200), alpha=0.6, hue=size_col)
    plt.title(f'{x_col} vs {y_col} (Bubble Size = {size_col})')
    plt.show()