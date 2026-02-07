import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def evaluate_predictions(y_true, y_pred):
    return {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": mean_squared_error(y_true, y_pred, squared=False),
    }


def compare_models(results: dict) -> pd.DataFrame:
    """
    results = {
        "naive": (y_true, y_pred),
        "linear": (y_true, y_pred),
        "tft": (y_true, y_pred)
    }
    """
    rows = []
    for model, (y_true, y_pred) in results.items():
        metrics = evaluate_predictions(y_true, y_pred)
        rows.append({
            "model": model,
            **metrics
        })

    results_df = pd.DataFrame(rows).sort_values("MAE")
    print("\nModel Comparison Results")
    print(results_df)
