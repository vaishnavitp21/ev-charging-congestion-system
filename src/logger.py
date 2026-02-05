import logging
import os


def setup_logger(name: str):
    """
    Configure and return a logger with standardized formatting.
    """
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
