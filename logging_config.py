# logging_config.py
import logging
import sys

def setup_logging():
    logger = logging.getLogger("uvicorn")  # Use uvicorn logger to integrate with FastAPI/uvicorn
    logger.setLevel(logging.INFO)

    # Create formatter - includes time, level, logger name, and message
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Create console handler and set level to INFO
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.handlers = []  # Clear existing handlers
    logger.addHandler(console_handler)

    return logger
