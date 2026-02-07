from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error


def run_station_mean_baseline() -> None:
    data_path = Path("data/processed/dataset.parquet")
    df = pd.read_parquet(data_path)

    # Time-based split
    cutoff = df["window_start"].quantile(0.8)
    train = df[df["window_start"] <= cutoff]
    val = df[df["window_start"] > cutoff]

    # Station-wise mean
    station_means = (
        train.groupby("station_name")["target_next_hour"]
        .mean()
        .to_dict()
    )

    global_mean = train["target_next_hour"].mean()

    # Predictions
    val["pred"] = val["station_name"].map(station_means).fillna(global_mean)

    mae = mean_absolute_error(val["target_next_hour"], val["pred"])
    rmse = mean_squared_error(val["target_next_hour"], val["pred"]) ** 0.5

    print("\n=== BASELINE: STATION MEAN PREDICTOR ===")
    print(f"Global mean target: {global_mean:.4f}")
    print(f"MAE : {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")


if __name__ == "__main__":
    run_station_mean_baseline()
