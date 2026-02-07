from pathlib import Path
from src.data.validate_raw import validate_raw_data


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    raw_dir = root / "data" / "raw"
    interim_dir = root / "data" / "interim"

    validate_raw_data(raw_dir, interim_dir)


if __name__ == "__main__":
    main()
