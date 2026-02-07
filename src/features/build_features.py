from pathlib import Path
import numpy as np
import pandas as pd


def build_features(interim_path: Path, processed_path: Path) -> None:
    """
    Build hourly congestion features from validated charging sessions.
    """

    in_file = interim_path / "validated.parquet"
    if not in_file.exists():
        raise FileNotFoundError(f"Missing validated data: {in_file}")

    df = pd.read_parquet(in_file)

    # Defensive schema check (FAANG-grade)
    required_cols = {"start_time", "end_time", "station_name"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # ------------------------------------------------------------------
    # Time bucketing
    # ------------------------------------------------------------------
    df["window_start"] = df["start_time"].dt.floor("h")

    # ------------------------------------------------------------------
    # Calendar features (deterministic per window)
    # ------------------------------------------------------------------
    df["hour"] = df["window_start"].dt.hour
    df["dayofweek"] = df["window_start"].dt.dayofweek
    df["is_weekend"] = df["dayofweek"].isin([5, 6]).astype(int)

    # Cyclic encoding
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    df["dow_sin"] = np.sin(2 * np.pi * df["dayofweek"] / 7)
    df["dow_cos"] = np.cos(2 * np.pi * df["dayofweek"] / 7)

    # ------------------------------------------------------------------
    # Aggregate to station-hour level
    # ------------------------------------------------------------------
    features = (
        df.groupby(["station_name", "window_start"])
          .agg(
              sessions_per_hour=("start_time", "count"),
              avg_session_minutes=(
                  "start_time",
                  lambda x: (
                      df.loc[x.index, "end_time"] - x
                  ).dt.total_seconds().mean() / 60.0
              ),

              # Preserve calendar features (constant within window)
              hour=("hour", "first"),
              dayofweek=("dayofweek", "first"),
              is_weekend=("is_weekend", "first"),
              hour_sin=("hour_sin", "first"),
              hour_cos=("hour_cos", "first"),
              dow_sin=("dow_sin", "first"),
              dow_cos=("dow_cos", "first"),
          )
          .reset_index()
    )

    # ------------------------------------------------------------------
    # Write output
    # ------------------------------------------------------------------
    processed_path.mkdir(parents=True, exist_ok=True)
    out_file = processed_path / "features.parquet"
    features.to_parquet(out_file, index=False)

    print(f"[OK] Features written to {out_file}")
