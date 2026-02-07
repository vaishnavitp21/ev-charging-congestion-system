from typing import List, Tuple
import pandas as pd

from pytorch_forecasting import TimeSeriesDataSet


def generate_walk_forward_cutoffs(
    df: pd.DataFrame,
    time_idx_col: str,
    min_train_size: int,
    forecast_horizon: int,
    step_size: int,
) -> List[int]:
    """
    Generate training cutoffs for walk-forward validation.

    Example:
    Train [0..T], validate [T+1 .. T+h]
    """

    max_time = df[time_idx_col].max()
    cutoffs = []

    cutoff = min_train_size
    while cutoff + forecast_horizon <= max_time:
        cutoffs.append(cutoff)
        cutoff += step_size

    return cutoffs


def build_validation_datasets(
    full_dataset: TimeSeriesDataSet,
    df: pd.DataFrame,
    time_idx_col: str,
    cutoffs: List[int],
) -> List[Tuple[TimeSeriesDataSet, TimeSeriesDataSet]]:
    """
    For each cutoff:
    - training dataset uses data <= cutoff
    - validation dataset predicts the future window
    """

    datasets = []

    for cutoff in cutoffs:
        training = TimeSeriesDataSet.from_dataset(
            full_dataset,
            df[df[time_idx_col] <= cutoff],
            stop_randomization=True,
        )

        validation = TimeSeriesDataSet.from_dataset(
            full_dataset,
            df[df[time_idx_col] > cutoff],
            predict=True,
            stop_randomization=True,
        )

        datasets.append((training, validation))

    return datasets
    print("\nTemporal Validation Results")
    print(metrics_df)
