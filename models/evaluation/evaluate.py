from models.evaluation.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
)


def evaluate_predictions(y_true, y_pred):
    """
    Evaluate predictions using shared metrics.

    Args:
        y_true (array-like): ground truth values
        y_pred (array-like): predicted values

    Returns:
        dict: metric_name -> value
    """
    results = {
        "mae": mean_absolute_error(y_true, y_pred),
        "rmse": root_mean_squared_error(y_true, y_pred),
    }

    return results
