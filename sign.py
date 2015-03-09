import webapp2
from google.appengine.ext import db
import models
import hashlib
import hmac
import views
import random
import string

class MainHandler(views.TempView):
	def page(self, template_values):
		self.render('sign.html', template_values)

	def get(self):
		template_values = {}
		self.page(template_values)
	
	def post(self):
		user = self.request.get("username")
		form_password = self.request.get("user_password")
		
		password = hmac.new('$31kljKoUlew349*#@98,dfskerwoI&#93j4l32kAJkl@!~lk23','',hashlib.sha512)
		password.update(form_password)
		password=password.hexdigest()
		
		p = db.Query(models.Users).filter("user_email = ", user)
		account = p.get()
		
		if account.password == password:
			cookie_data = self.set_cookie(user, password)
			account.session_key = cookie_data[1]
			account.salt = cookie_data[0]
			account.put()
			
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.headers.add_header('Set-Cookie', 'user=' + str(user) + '; Path=/')
			self.response.headers.add_header('Set-Cookie', 'session=' + str(account.session_key) + '; Path=/')
		
			self.redirect('http://zoinkpage.appspot.com')
			
		else:
			self.response.out.write("account not active")
		
		
	def set_cookie(self,email_address, password):
		salt = ''.join(random.choice(string.letters) for x in xrange(7))
		session_key = hashlib.sha256(email_address + password + salt).hexdigest()
		return salt, session_key	

app = webapp2.WSGIApplication([('/sign-in', MainHandler)],
		                     debug=True)