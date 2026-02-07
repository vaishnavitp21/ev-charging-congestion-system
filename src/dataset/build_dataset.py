from pathlib import Path
import pandas as pd


def build_dataset(processed_path: Path) -> None:
    """
    Merge features and target into final ML dataset.
    """

    features_file = processed_path / "features.parquet"
    target_file = processed_path / "target.parquet"

    if not features_file.exists():
        raise FileNotFoundError(f"Missing features: {features_file}")
    if not target_file.exists():
        raise FileNotFoundError(f"Missing target: {target_file}")

    X = pd.read_parquet(features_file)
    y = pd.read_parquet(target_file)

    # ---- Defensive schema checks (FAANG-style) ----
    required_feature_cols = {"station_name", "window_start"}
    required_target_cols = {"station_name", "window_start", "target_next_hour"}

    if not required_feature_cols.issubset(X.columns):
        raise ValueError(
            f"Features missing columns: {required_feature_cols - set(X.columns)}"
        )

    if not required_target_cols.issubset(y.columns):
        raise ValueError(
            f"Target missing columns: {required_target_cols - set(y.columns)}"
        )

    # ---- Merge ----
    dataset = X.merge(
        y[["station_name", "window_start", "target_next_hour"]],
        on=["station_name", "window_start"],
        how="inner",
        validate="one_to_one",
    )

    out_file = processed_path / "dataset.parquet"
    dataset.to_parquet(out_file, index=False)

    print(f"[OK] Dataset written to {out_file}")
