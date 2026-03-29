import logging
import logging.handlers
import os
from typing import List


def _setup_secure_logger(
    logger_name: str, 
    log_dir: str = ".logs",
    log_filename: str = "process.log",
    max_bytes: int = 5_000_000,  # 5MB
    backup_count: int = 5
) -> logging.Logger:
    """
    Configure logger with security best practices.
    
    Args:
        logger_name: Name of the logger
        log_dir: Directory for logs (default: .logs)
        log_filename: Name of log file
        max_bytes: Max size before rotation (5MB default)
        backup_count: Number of backup files to keep
        
    Returns:
        Configured logger instance
    """
    # Create logs directory securely with restricted permissions
    os.makedirs(log_dir, mode=0o700, exist_ok=True)
    
    log_path = os.path.join(log_dir, log_filename)
    
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    
    # Clear existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Use rotating file handler to prevent disk bloat
    rotating_handler = logging.handlers.RotatingFileHandler(
        log_path,
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    
    # Format logs with timestamp and severity
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    rotating_handler.setFormatter(formatter)
    
    logger.addHandler(rotating_handler)
    
    return logger


# Initialize logger at module level with secure configuration
logger = _setup_secure_logger(__name__)


def apply_multiplier(value: float, multiplier: float = 1.15) -> float:
    """Multiply a value by a given multiplier."""
    _validate_numeric(value)
    _validate_numeric(multiplier)

    return value * multiplier


def format_currency(value: float) -> str:
    """Format value as a readable string."""
    return f"Total: {value:.2f}"


def process_values(values: List[float], multiplier: float = 1.15) -> List[float]:
    """
    Core processing function (pure function).
    Only computes values, no side effects.
    """
    _validate_list(values)

    return [apply_multiplier(v, multiplier) for v in values]


def display_results(values: List[float]) -> None:
    """Responsible ONLY for printing."""
    for value in values:
        print(format_currency(value))


def log_results(values: List[float]) -> None:
    """Responsible ONLY for logging."""
    logger.info(f"Processed values: {values}")


# -------- VALIDATION -------- #

def _validate_numeric(value: float) -> None:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"Invalid numeric value: {value}")


def _validate_list(values: List[float]) -> None:
    if not values:
        raise ValueError("Input list cannot be empty")

    for v in values:
        _validate_numeric(v)

if __name__ == "__main__":
    sample_values = [10, 20, 30]

    processed = process_values(sample_values)
    display_results(processed)
    log_results(processed)