from pathlib import Path
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt


def run_decision_tree():
    root = Path(__file__).resolve().parents[2]
    data_path = root / "data" / "processed" / "dataset.parquet"

    df = pd.read_parquet(data_path).sort_values("window_start")

    FEATURES = [
        "sessions_per_hour",
        "avg_session_minutes",
    ]

    TARGET = "target_next_hour"

    split_time = df["window_start"].quantile(0.8)

    train = df[df["window_start"] < split_time]
    test = df[df["window_start"] >= split_time]

    X_train = train[FEATURES]
    y_train = train[TARGET]
    X_test = test[FEATURES]
    y_test = test[TARGET]

    model = DecisionTreeRegressor(
        max_depth=5,
        min_samples_leaf=50,
        random_state=42,
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = sqrt(mean_squared_error(y_test, preds))

    print("\n=== DECISION TREE: TEMPORAL FEATURES ===")
    print(f"MAE:  {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")


if __name__ == "__main__":
    run_decision_tree()
