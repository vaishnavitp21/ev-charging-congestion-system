from pathlib import Path
import pandas as pd


def inspect_dataset() -> None:
    root = Path(__file__).resolve().parents[2]
    dataset_path = root / "data" / "processed" / "dataset.parquet"

    df = pd.read_parquet(dataset_path)

    print("\n=== DATASET SHAPE ===")
    print(df.shape)

    print("\n=== COLUMNS ===")
    for col in df.columns:
        print(col)

    print("\n=== SAMPLE ROWS ===")
    print(df.head(5))

    print("\n=== TARGET STATS ===")
    print(df["target_next_hour"].describe())

    print("\n=== TIME RANGE ===")
    print(df["window_start"].min(), "→", df["window_start"].max())


if __name__ == "__main__":
    inspect_dataset()
