import logging
from logging.handlers import RotatingFileHandler
import sys
import os

def setup_logger(name: str = "shop_bot", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # already configured

    logger.setLevel(level)

    log_dir = os.path.abspath(os.getenv("LOG_DIR", "."))
    os.makedirs(log_dir, exist_ok=True)
    logfile = os.path.join(log_dir, "bot.log")

    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s — %(message)s")

    file_handler = RotatingFileHandler(logfile, maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    file_handler.setFormatter(fmt)
    file_handler.setLevel(level)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(fmt)
    stream_handler.setLevel(level)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.propagate = False
    return logger
