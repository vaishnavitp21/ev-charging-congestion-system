from pathlib import Path
from src.features.build_features import build_features


def main() -> None:
    root = Path(__file__).resolve().parents[1]

    interim_path = root / "data" / "interim"
    processed_path = root / "data" / "processed"

    build_features(
        interim_path=interim_path,
        processed_path=processed_path,
    )


if __name__ == "__main__":
    main()
