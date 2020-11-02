import logging
import logging.config

from api.config import settings

class GunicornFilter(logging.Filter):
  def filter(self, record: logging.LogRecord) -> bool:
    if '"- - HTTTP/1.0" 0 0' in record.msg:
      return False
    else:
      return True

def setup_logging():
  config = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"gunicorn_filter": {"()": GunicornFilter}},
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
        "filters": ["gunicorn_filter"],
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
