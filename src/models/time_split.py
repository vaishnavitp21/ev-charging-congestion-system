from pathlib import Path
import pandas as pd


def time_based_split(
    data_path: Path,
    split_date: str = "2020-01-01"
):
    """
    Split dataset into train / validation using time-based cutoff.
    """

    df = pd.read_parquet(data_path)

    assert "window_start" in df.columns, "window_start missing"
    assert "target_next_hour" in df.columns, "target missing"

    split_ts = pd.to_datetime(split_date)

    train_df = df[df["window_start"] < split_ts].copy()
    val_df = df[df["window_start"] >= split_ts].copy()

    print("=== TIME SPLIT SUMMARY ===")
    print(f"Split date        : {split_ts}")
    print(f"Train rows        : {len(train_df)}")
    print(f"Validation rows   : {len(val_df)}")
    print()
    print("Train time range  :", train_df["window_start"].min(), "→", train_df["window_start"].max())
    print("Val time range    :", val_df["window_start"].min(), "→", val_df["window_start"].max())

    return train_df, val_df


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    dataset = root / "data" / "processed" / "dataset.parquet"
    time_based_split(dataset)
