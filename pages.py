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
import webapp2
import views
import data_source
from google.appengine.ext import db
import models
import mail

class TeamHandler(views.TempView):
	def get(self):
		template_values ={}
		self.render('the-team.html',template_values)
	
class ContactHandler(views.TempView):
	def get(self):
		template_values ={}
		self.render('contact.html',template_values)
		
	def post(self):
		name = self.request.get("name")
		email = self.request.get("email")
		response = self.request.get("response")

		if name and email and response:
			form = models.Contact(name=name, email_address = db.Email(email), response = response)
			form.put()
			message = mail.ContactMailer()
			message.customer_email(name,email)
			message.staff_email(name,email,response)
			self.redirect('/pages/contact')
		
		else:
			self.redirect('/')
		
class SuggestionHandler(views.TempView):
	def get(self):
		template_values = {}
		self.render('suggestions.html',template_values)
		
		
class What_It_MeansHandler(views.TempView):
	def get(self):
		template_values = {}
		self.render('what_it_means.html',template_values)
		
class PrivacyHandler(views.TempView):
	def get(self):
		template_values ={}
		self.render('privacy.html', template_values)
		
class RefundHandler(views.TempView):
	def get(self):
		template_values ={}
		self.render('refunds.html', template_values)
		
app = webapp2.WSGIApplication([('/pages/the-team',TeamHandler),
							   ('/pages/contact', ContactHandler),
							   ('/pages/suggestions', SuggestionHandler),
							   ('/pages/partnerships/what-it-means', What_It_MeansHandler),
						       ('/pages/privacy', PrivacyHandler),
							   ('/pages/refunds', RefundHandler)],
		                        debug=True)