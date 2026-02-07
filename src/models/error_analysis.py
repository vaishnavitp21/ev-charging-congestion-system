from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

DATASET_PATH = Path("data/processed/dataset.parquet")

def main():
    df = pd.read_parquet(DATASET_PATH)

    # Time-based split (reuse same cutoff)
    split_date = pd.Timestamp("2020-01-01")
    train = df[df["window_start"] < split_date]
    val = df[df["window_start"] >= split_date]

    FEATURES = [
        "sessions_per_hour",
        "avg_session_minutes",
        "hour_sin",
        "hour_cos",
        "dow_sin",
        "dow_cos",
        "is_weekend",
    ]

    X_train = train[FEATURES]
    y_train = train["target_next_hour"]
    X_val = val[FEATURES]
    y_val = val["target_next_hour"]

    model = DecisionTreeRegressor(max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_val)
    val = val.copy()
    val["abs_error"] = np.abs(y_val - preds)
    print("\n=== ERROR BY HOUR (TOP 10) ===")
    print(
        val.groupby("hour")["abs_error"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n=== ERROR BY STATION (TOP 10) ===")
    print(
        val.groupby("station_name")["abs_error"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n=== WEEKEND VS WEEKDAY ERROR ===")
    print(
        val.groupby("is_weekend")["abs_error"]
        .mean()
        .rename({0: "Weekday", 1: "Weekend"})
    )


    # TODO: error slices here
    # hour, station_name, is_weekend

if __name__ == "__main__":
    main()
