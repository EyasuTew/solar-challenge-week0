import matplotlib.pyplot as plt
import seaborn as sns
from typing import List

def plot_distributions(df: pd.DataFrame, columns: List[str], ncols: int = 3):
    """Subplots of histograms for key vars."""
    nrows = (len(columns) + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols*5, nrows*4))
    axes = axes.flatten() if nrows > 1 else [axes]
    for i, col in enumerate(columns):
        sns.histplot(df[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
    plt.tight_layout()
    plt.show()