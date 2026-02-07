from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error


def run_lag1_baseline() -> None:
    df = pd.read_parquet("data/processed/dataset.parquet")

    # Sort for temporal correctness
    df = df.sort_values(["station_name", "window_start"])

    # Lag-1 feature
    df["pred"] = df.groupby("station_name")["sessions_per_hour"].shift(1)

    # Drop rows without lag
    df = df.dropna(subset=["pred"])

    # Time-based split
    cutoff = df["window_start"].quantile(0.8)
    val = df[df["window_start"] > cutoff]

    mae = mean_absolute_error(val["target_next_hour"], val["pred"])
    rmse = mean_squared_error(val["target_next_hour"], val["pred"]) ** 0.5

    print("\n=== BASELINE: LAG-1 TEMPORAL PREDICTOR ===")
    print(f"MAE : {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")


if __name__ == "__main__":
    run_lag1_baseline()
