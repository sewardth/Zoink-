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
import random
import hashlib
import hmac
import re
from string import letters
from google.appengine.api import users
from google.appengine.ext import db
import models

jinja_environment = jinja2.Environment(autoescape = True, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')))

secret = 'fj.3WexFF.90!54Trds?.-1qxFR?53$.Gqu,gTr3^js234Ls'



class TempView(webapp2.RequestHandler):
	def PathResponse(self):
		path = self.request.path
		if path == '/':
			response = 'Zoink! - The awesome gadget rental company'
		else:
		    x=0
		    while x != -1:
		        start = x
		        x = path.find('/',x+1)
			name = path[start+1:]
			#value = re.sub(['-'],' ', name)
		    response = 'Zoink! - ' + name
		return response

	def user_check(self):
		user = self.request.cookies.get('user', 0)
		session = self.request.cookies.get('session', 0)
		if user:
			query = db.Query(models.Users).filter("user_email = ", user)
			q = query.get()
			if q.session_key == session:
				greeting = q.first_name
			else: 
				greeting = False
				
		else:
			greeting = False
			
		return greeting
	
	def PageCreator(self, page, template_values):
		self.response.headers['Content-Type'] = 'text/html'
		header = jinja_environment.get_template('header.html')
		footer = jinja_environment.get_template('footer.html')
		path = self.PathResponse()
		user = self.user_check()
		cart_count = self.cart_count(self.request.cookies.get('user',False))
		values = template_values
		values['direct'] = self.request.path
		values['cart_count'] = int(cart_count)
		values['page_title'] = path
		values['user'] = user
		values['userid'] = self.request.cookies.get('user',False)
		page = jinja_environment.get_template(page)
		temp_header = header.render(values)
		temp_page = page.render(values)
		temp_footer = footer.render(values)
		view = temp_header + temp_page + temp_footer
		return view
	
	def render(self, page, template_values):
		pageview= self.PageCreator(page, template_values)
		self.response.out.write(pageview)

	def get_path(self):
		path = self.request.path
		return path
		
	def get_url(self):
		url = self.request.url
		return url
		
	def cart_count(self, userid):
		p = models.Cart.all()
		p = db.Query(models.Cart).filter("userid = ", userid)
		cart_products = p.fetch(100)
		return len(cart_products)
		
	