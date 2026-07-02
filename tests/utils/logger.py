import logging


def get_logger(name: str, logger_level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.FileHandler(f"/tmp/{name}.log", mode="w")
    handler.setLevel(logger_level)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s"))

    logger.addHandler(handler)

    logger.debug("file handler works")
    return logger
