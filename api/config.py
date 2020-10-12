import argparse

from api.util.vyper import settings

settings = settings

parser = argparse.ArgumentParser(description="Runs the API")


#General
g = parser.add_argument_group("general")
g.add_argument("--app-name",
	type=str, 
	default="api", 
	help="Application and process name. (default %(default)s)",
)
g.add_argument("--env-name",
	type=str,
	default='LOCAL',
	choices=["LOCAL","DOCKER","PROD"],
	help="Environment to run as. (default %(default)s)",
	)
g.add_argument("--environment-variables-prefix",
	type=str,
	default="app",
	help="Prefix for environment variables (default %(default)s)",
	)


#Gunicorn
gu = parser.add_argument_group("Gunicorn")
gu.add_argument("--access-log",
	type=str,
	default="-",
	help="Where to store the access logs. (default %(default)s)",
	)
gu.add_argument("--access-log-format",
	type=str,
	default='%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s',
	help="Gunicorn access log format. (default %(default)s)",
	)
gu.add_argument("--bind",
	type=str,
	default="127.0.0.1:5000",
	help="The socket to bind to. (default %(default)s)",
	)
gu.add_argument("--error-log",
	type=str,
	default="-",
	help="Where to store the error logs. (default %(default)s)",
	)
gu.add_argument("--keep-alive",
	type=int,
	default=650,
	help="The number of seconds to wait for requests on a Keep-Alive connection. (default %(default)s)",
	)
gu.add_argument("--max-requests",
	type=int,
	default=0,
	help="The maximum number of requests a worker will process before restarting. (default %(default)s)",
	)
gu.add_argument("--max-requests-jitter",
	type=int,
	default=0,
	help="The maximum jitter to add to the max_requests setting. (default %(default)s)",
	)
gu.add_argument("--timeout",
	type=int,
	default=240,
	help="Workers silent for more than this many seconds are killed and restarted. (default %(default)s)",
	)
gu.add_argument("--worker-class",
	type=str,
	default="egg:meinheld#gunicorn_worker",
	help="The type of worker to use. (default %(default)s)",
	)
gu.add_argument("--workers",
	type=int,
	default=1,
	help="The number of workers to use. (default %(default)s)",
	)
gu.add_argument("--reload",
	action='store_true',
	default=False,
	help="Reload Gunicorn if code is changed (default %(default)s",
	)


#Logs
l = parser.add_argument_group("Logs")
l.add_argument("--log-format",
	type=str,
	default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
	help="Log format (default %(default)s)",
	)
l.add_argument("--log-date-format",
	type=str,
	default="%Y-%m-%d %H:%M:%S %z",
	help="Log date format (default %(default)s)",
	)
l.add_argument("--log-handlers",
	type=str,
	default="console",
	help="Log handlers (default %(default)s)",
	)
l.add_argument("--log-level",
	type=str,
	default="DEBUG",
	help="Log level (default %(default)s)",
)


#MongoDB
m = parser.add_argument_group("MongoDB")
m.add_argument("--mongo-uri",
	type=str,
	default="mongodb://localhost:27017/",
	help="MongoDB URI (default %(default)s)",
	)
m.add_argument("--mongo-user",
	type=str,
	default=None,
	help="Mongo username (default %(default)s)",
	)
m.add_argument("--mongo-password",
	type=str,
	default=None,
	help="Mongo passwords (default %(default)s)",
	)









