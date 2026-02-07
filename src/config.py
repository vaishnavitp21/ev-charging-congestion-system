from pathlib import Path
import yaml


def load_data_paths(config_path: Path) -> dict:
    """
    Load data paths from YAML configuration.
    """
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    return config["data"]
