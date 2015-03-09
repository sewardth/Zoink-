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
import jinja2
import os
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.ext import db
import models
import views
import mail
import hashlib
import hmac

jinja_environment = jinja2.Environment(autoescape = True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))


class templategenerator:
	def __init__(self, page, template_values):
		#header = jinja_environment.get_template('admin_header.html')
		page = jinja_environment.get_template(page)
		#self.temp_header = header.render(template_values)
		self.temp_page = page.render(template_values)
	
	def print_page(self):
		template = self.temp_page
		return template

class getuser:
	def __init__(self, path):
		user = users.get_current_user()
		
		if user:
			self.admin = user.nickname() 
			self.admin_logout = users.create_logout_url(path)
		else:
		   	self.admin_login = users.create_login_url(path)
			
		
	def admin(self):
		return self.admin
		
	def admin_logout(self):
		return self.admin_logout
	

class MainHandler(webapp2.RequestHandler):	
	def get(self):
		path = self.request.path
		user = getuser(path)
		admin = user.admin
		admin_logout = user.admin_logout
		page = 'admin.html'
		products = models.Product.all()
		p = db.Query(models.SignUp).filter("approved = ", 0)
		registrations = p.fetch(100)
		
		
		template_values = {'admin': admin, 'admin_logout':admin_logout, 'registrations':registrations}
		template = templategenerator(page, template_values)
		
		self.response.out.write(template.print_page())

	def post(self):
		if self.request.get("product_registration") == 'Create Product':
			self.product_register()
		elif self.request.get("product_update") == 'Update Product':
			self.product_update()
		else:
			self.register_user()
			
	def product_register(self):
		p = models.Product()
		p.prod_title = self.request.get("prod_title")
		url = '/products/'+p.prod_title
		p.prod_url = url.replace(" ","-")
		p.prod_manufacturer = self.request.get("prod_manufacturer")
		p.prod_price = float(self.request.get("price"))
		p.starting_inventory  = int(self.request.get("starting_inventory"))
		p.youtube = db.Link(self.request.get("youtube"))
		large = images.resize(self.request.get("prod_image"),520,345)
		normal = images.resize(self.request.get("prod_image"),290,193)
		thumb = images.resize(self.request.get("prod_image"),150,100)
		p.image_large = db.Blob(large)
		p.image_normal = db.Blob(normal)
		p.image_thumb = db.Blob(thumb)
		p.zoink_perspective = db.Text(self.request.get("zoink_perspective"))
		p.prod_overview = db.Text(self.request.get("overview"))
		p.need_to_know = db.Text(self.request.get("need_to_know"))
		p.put()
		
		self.redirect('/admin')
		
	def register_user(self):
		user_id = self.request.get("date")
		email = self.request.get("email")
		first_name = self.request.get("first_name")
		last_name = self.request.get("last_name")
		link_creator = hmac.new('F3nmE3klwk,!.,3jlkn&$j53l7#2;12@m,mKjkjKJIODSJHFneklj43kl24j89ejf89enu','',hashlib.sha256)
		link_creator.update(user_id)
		secure_link=link_creator.hexdigest()
		unique_id = 'http://zoinkpage.appspot.com' + '/accounts/activation/' + secure_link
		query = db.Query(models.SignUp).filter("email_address = ", email)
		record = query.get()
		record.activation_url = unique_id
		record.approved = 1
		record.put()
		message = mail.ApprovedMailer()
		message.account_email(first_name, last_name, email, unique_id)	
		self.redirect("/admin")	
		
		
		
app = webapp2.WSGIApplication([('/admin', MainHandler)],
		                     debug=True)