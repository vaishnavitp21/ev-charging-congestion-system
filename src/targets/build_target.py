from pathlib import Path
import pandas as pd


def build_target(interim_path: Path, processed_path: Path) -> None:
    """
    Build next-hour congestion target.
    Target = number of sessions in the NEXT hour for a station.
    """

    in_file = interim_path / "validated.parquet"
    if not in_file.exists():
        raise FileNotFoundError(f"Missing validated data: {in_file}")

    df = pd.read_parquet(in_file)

    # Defensive schema check
    required_cols = {"start_time", "station_name"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Hour bucket (lowercase 'h' is REQUIRED)
    df["window_start"] = df["start_time"].dt.floor("h")

    hourly = (
        df.groupby(["station_name", "window_start"])
          .size()
          .rename("sessions_this_hour")
          .reset_index()
    )

    # Target = next hour load
    hourly["target_next_hour"] = (
        hourly
        .groupby("station_name")["sessions_this_hour"]
        .shift(-1)
    )

    target = hourly.dropna(subset=["target_next_hour"]).copy()

    processed_path.mkdir(parents=True, exist_ok=True)
    out_file = processed_path / "target.parquet"
    target.to_parquet(out_file, index=False)

    print(f"[OK] Target written to {out_file}")
