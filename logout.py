import webapp2

class logoutHandler(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.headers.add_header('Set-Cookie', 'user=' + '' + '; Path=/')
		self.response.headers.add_header('Set-Cookie', 'session=' + '' + '; Path=/')
		path=self.request.get("path")
		self.redirect(str(path))


app = webapp2.WSGIApplication([('/logout', logoutHandler)],
		                        debug=True)