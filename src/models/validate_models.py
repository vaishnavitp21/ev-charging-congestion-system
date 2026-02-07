from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor


def load_split():
    root = Path(__file__).resolve().parents[2]
    df = pd.read_parquet(root / "data" / "processed" / "dataset.parquet")

    split_ts = pd.to_datetime("2020-01-01")

    train = df[df["window_start"] < split_ts].copy()
    val = df[df["window_start"] >= split_ts].copy()

    features = [
        "sessions_per_hour",
        "avg_session_minutes",
        "hour",
        "dayofweek",
        "is_weekend",
        "hour_sin",
        "hour_cos",
        "dow_sin",
        "dow_cos",
    ]

    X_train = train[features]
    y_train = train["target_next_hour"]

    X_val = val[features]
    y_val = val["target_next_hour"]

    return X_train, y_train, X_val, y_val


import numpy as np

def evaluate(name, y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"{name:<30} MAE={mae:.4f} | RMSE={rmse:.4f}")


if __name__ == "__main__":
    X_train, y_train, X_val, y_val = load_split()

    print("\n=== VALIDATION RESULTS (TIME-BASED) ===\n")

    # Baseline: global mean
    mean_pred = y_train.mean()
    evaluate(
        "Baseline: Global Mean",
        y_val,
        [mean_pred] * len(y_val),
    )

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    evaluate(
        "Linear Regression",
        y_val,
        lr.predict(X_val),
    )

    # Decision Tree (simple, untuned)
    dt = DecisionTreeRegressor(max_depth=6, random_state=42)
    dt.fit(X_train, y_train)
    evaluate(
        "Decision Tree",
        y_val,
        dt.predict(X_val),
    )
