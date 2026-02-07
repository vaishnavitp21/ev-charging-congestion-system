from pathlib import Path
from src.dataset.build_dataset import build_dataset


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    processed_path = root / "data" / "processed"

    build_dataset(processed_path)


if __name__ == "__main__":
    main()
