#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import views
import webapp2
from google.appengine.ext import db
import re
import models	
import mail
	
class MainHandler(views.TempView):
	def page(self, template_values):
		self.render('home.html', template_values)
		
	def get(self):
		template_values = {'first_name': "", 'last_name':"", 'email_address':""}
		self.page(template_values)
		
	def post(self):
		first_name = self.request.get("first_name")
		last_name = self.request.get("last_name")
		email_address = self.request.get("email_address")
		
		if first_name and last_name and email_address:
			p = db.Query(models.SignUp).filter("email_address = ", email_address)
			q = p.get()
			if q:
				template_values = {'first_name': "", 'last_name': "", 'email_address': "",'error': 'The email address listed is already signed up!'}
				self.page(template_values)
			else:
				data = models.SignUp(first_name = first_name, last_name = last_name, email_address = db.Email(email_address))
				data.put()
				template_values = {'first_name': "", 'last_name': "", 'email_address': "",'error': 'Thank you for signing up!'}
				self.page(template_values)
				message = mail.SignUpMailer()
				message.email_response(first_name, email_address)
			
			
		else:
			template_values = {'first_name': first_name, 'last_name': last_name, 'email_address': email_address, 'error': 'All fields must be complete'}
			self.page(template_values)
			


app = webapp2.WSGIApplication([('/', MainHandler)],debug=True)