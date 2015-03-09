import models
import mail
import views
import string
import random
import webapp2
from google.appengine.ext import db
import hashlib
import hmac


class ActivationHandler(views.TempView):
	def get(self):
		link = self.request.url
		query = db.Query(models.SignUp).filter("activation_url = ", link)
		q = query.get()
		template_values ={'user_email': q.email_address,
						  'first_name': q.first_name,
						  'last_name' : q.last_name}
		self.render('activation.html',template_values)


	def post(self):
		first_name = self.request.get("first_name")
		last_name = self.request.get("last_name")
		email_address = self.request.get("email_address")
		first_password = self.request.get("first_password")
		second_password = self.request.get("second_password")
		
		if first_password == second_password:
			password = hmac.new('$31kljKoUlew349*#@98,dfskerwoI&#93j4l32kAJkl@!~lk23','',hashlib.sha512)
			password.update(first_password)
			password=password.hexdigest()
			
			cookie_data = self.set_cookie(email_address, password)
			
			
			data = models.Users()
			data.user_email = db.Email(email_address)
			data.password = password
			data.first_name = first_name
			data.last_name = last_name
			data.session_key = cookie_data[1]
			data.salt = cookie_data[0]
			data.put()
			
			self.response.headers.add_header(
					'Set-Cookie',
					'session = %s; user = %s; path ="/"; domain = "zoinkpage.appspot.com"' %(str(cookie_data[1]), str(email_address)))
			self.redirect("http://zoinkpage.appspot.com")
			
	def set_cookie(self,email_address, password):
		salt = ''.join(random.choice(string.letters) for x in xrange(7))
		session_key = hashlib.sha256(email_address + password + salt).hexdigest()
		return salt, session_key



app = webapp2.WSGIApplication([('/accounts/activation.*',ActivationHandler)],
		                     debug=True)