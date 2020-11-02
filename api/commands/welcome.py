import falcon
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


class Welcome(object):
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200
		resp.body = ("Welcome to the Bambinito API\n"\
			"Please contact bambinito.dev@gmail.com for any questions/inquiries...\n\n"\
			"Hostname: {}\n"\
			"Ip: {}\n".format(hostname, ip))