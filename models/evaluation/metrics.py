import numpy as np


def mean_absolute_error(y_true, y_pred):
    """
    Mean Absolute Error (MAE).

    Ignores NaN values in predictions.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    mask = ~np.isnan(y_pred)
    if not np.any(mask):
        raise ValueError("All predictions are NaN")

    return np.mean(np.abs(y_true[mask] - y_pred[mask]))


def root_mean_squared_error(y_true, y_pred):
    """
    Root Mean Squared Error (RMSE).

    Ignores NaN values in predictions.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    mask = ~np.isnan(y_pred)
    if not np.any(mask):
        raise ValueError("All predictions are NaN")

    return np.sqrt(np.mean((y_true[mask] - y_pred[mask]) ** 2))
