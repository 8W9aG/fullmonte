"""Plot a Monte Carlo simulation."""

from typing import Any

import pandas as pd


def plot(df: pd.DataFrame) -> Any:
    """Plot the monte carlo simulation."""
    return df.plot(legend=False)
