"""Simulate a monte carlo run."""

from typing import Optional

import numpy as np
import pandas as pd


def _create_column_values(
    arr: np.ndarray, length: int, worst_days: int, first_value: float
) -> np.ndarray:
    first_array = np.sort(arr)[-worst_days:] if worst_days > 0 else np.array([])
    return np.concatenate(
        (
            np.array([first_value]),
            first_array,
            np.random.normal(np.mean(arr), np.std(arr), length),
        )
    ).cumprod()


def simulate(
    returns: pd.Series,
    simulations: int = 1000,
    worst_days: Optional[int] = None,
    length: int = 252 * 2,
) -> pd.DataFrame:
    """Run a simulation on a returns series."""
    arr = returns.pct_change().dropna().to_numpy() + 1.0
    return pd.DataFrame(
        data={
            f"{x}_sim": _create_column_values(
                arr, length, 0 if worst_days is None else worst_days, returns.iloc[-1]
            )
            for x in range(simulations)
        }
    )
