from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def run_linear_model() -> None:
    df = pd.read_parquet("data/processed/dataset.parquet")

    # Sort for safety
    df = df.sort_values(["station_name", "window_start"])

    # Temporal features
    df["hour"] = df["window_start"].dt.hour
    df["dayofweek"] = df["window_start"].dt.dayofweek
    df["lag_1"] = df.groupby("station_name")["sessions_per_hour"].shift(1)

    df = df.dropna()

    features = [
        "sessions_per_hour",
        "avg_session_minutes",
        "hour",
        "dayofweek",
        "lag_1",
    ]

    X = df[features]
    y = df["target_next_hour"]

    # Time-based split
    cutoff = df["window_start"].quantile(0.8)
    train = df["window_start"] <= cutoff
    val = df["window_start"] > cutoff

    model = LinearRegression()
    model.fit(X[train], y[train])

    preds = model.predict(X[val])

    mae = mean_absolute_error(y[val], preds)
    rmse = mean_squared_error(y[val], preds) ** 0.5

    print("\n=== LINEAR REGRESSION: TEMPORAL FEATURES ===")
    print(f"MAE : {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")

    print("\nTop coefficients:")
    for name, coef in sorted(zip(features, model.coef_), key=lambda x: abs(x[1]), reverse=True):
        print(f"{name:22s} {coef:+.4f}")


if __name__ == "__main__":
    run_linear_model()
