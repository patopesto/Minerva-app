import logging
import json
import falcon

from api.config import parser, settings
from api.util.vyper import setup_vyper
from api.util.logging import setup_logging

from .commands import routes

logger = logging.getLogger(__name__)

def configure(**overrides):
	logging.getLogger("pymongo").setLevel(level=logging.DEBUG)
	logging.getLogger("requests").setLevel(level=logging.INFO)
	logging.getLogger("urllib3").setLevel(level=logging.INFO)
	logging.getLogger("apscheduler").setLevel(level=logging.DEBUG)
	logging.getLogger('vyper').setLevel(level=logging.WARNING)
	logging.getLogger('werkzeug').setLevel(level=logging.INFO)

	setup_vyper(parser, overrides)
	setup_logging()



def create_app():
	# falcon.API instances are callable WSGI apps
	app = falcon.API()
	routes.setup_routes(app)
	return app


def start():
	pass



