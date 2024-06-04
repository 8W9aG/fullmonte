"""Plot a Monte Carlo simulation."""

from typing import Any

import pandas as pd


def plot(df: pd.DataFrame) -> Any:
    """Plot the monte carlo simulation."""
    old_backend = pd.options.plotting.backend
    pd.options.plotting.backend = "matplotlib"
    fig = df.plot(legend=False)
    pd.options.plotting.backend = old_backend
    return fig
