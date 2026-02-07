from pathlib import Path
from src.targets.build_target import build_target


def main() -> None:
    root = Path(__file__).resolve().parents[1]

    interim_path = root / "data" / "interim"
    processed_path = root / "data" / "processed"

    build_target(
        interim_path=interim_path,
        processed_path=processed_path,
    )


if __name__ == "__main__":
    main()
