"""Logging configuration"""
import logging
import logging.handlers
from config import settings
from pathlib import Path


def setup_logging():
    """Setup logging configuration"""
    log_dir = Path(settings.log_file).parent
    log_dir.mkdir(parents=True, exist_ok=True)

    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level)

    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        settings.log_file, maxBytes=10485760, backupCount=5  # 10MB files
    )
    file_handler.setLevel(settings.log_level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(settings.log_level)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    return root_logger
