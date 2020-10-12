import falcon

class Welcome(object):
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200
		resp.body = ('Welcome to the Bambinito API\nPlease contact bambinito.dev@gmail.com for any questions/inquiries...')