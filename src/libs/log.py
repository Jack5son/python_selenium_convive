import logging

_loggers = {}


def logger(name: str) -> logging.Logger:
    logger_ = _loggers.get(name)

    if logger_ is None:
        logger_ = logging.getLogger(name)
        logger_.setLevel(logging.DEBUG)

        formatter = logging.Formatter(fmt=(
                '[%(levelname)s] - '
                '[%(name)s:%(lineno)d] - '
                '[%(asctime)s] -> '
                '%(message)s'
            ),
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)

        logger_.addHandler(handler)
        _loggers[name] = logger_

    return logger_
