import logging
import logging.config

from api.config import settings


def setup_logging():
  config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
      "standard": {
        "format": settings.get("LOG_FORMAT"),
        "datefmt": settings.get("LOG_DATE_FORMAT"),
      }
    },
    "handlers": {
      "console": {
        "class": "logging.StreamHandler",
        "formatter": "standard",
        "level": "DEBUG",
        "stream": "ext://sys.stdout",
      }
    },
    "loggers": {
      "": {
        "handlers": settings.get("LOG_HANDLERS").split(","),
        "level": settings.get("LOG_LEVEL"),
      }
    },
  }
  logging.config.dictConfig(config)
