from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def run_baseline() -> None:
    data_path = Path("data/processed/dataset.parquet")
    df = pd.read_parquet(data_path)

    # Time-based split (no leakage)
    df = df.sort_values("window_start")
    split_idx = int(len(df) * 0.8)

    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]

    y_train = train["target_next_hour"]
    y_test = test["target_next_hour"]

    # Mean baseline
    baseline_value = y_train.mean()
    y_pred = np.full_like(y_test, fill_value=baseline_value, dtype=float)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    print("\n=== BASELINE: MEAN PREDICTOR ===")
    print(f"Train mean target: {baseline_value:.4f}")
    print(f"MAE : {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")


if __name__ == "__main__":
    run_baseline()
