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
import data_source
import views
from google.appengine.ext import db
import models
from google.appengine.api import images

class ProductHandler(views.TempView):
	def page(self, template_values):
		self.render('product.html', template_values)
	
	def get(self):
		path = self.get_path()
		url = self.get_url()	
		p = db.Query(models.Product).filter("prod_url = ", path)
		q = p.get()
		images=data_source.products()
		
		
		template_values={'prod_title': q.prod_title,
						 'prod_path': path,
						 'prod_comp': q.prod_manufacturer,
						 'zoink_perspective': q.zoink_perspective,
						 'prod_price':  '%.2f' %q.prod_price,
						 'prod_overview': q.prod_overview,
						 'need_to_know': q.need_to_know,
						 'prod_video': q.youtube,
						 'prod_url': url,
						 'prod_image': images[path]}	
		
		self.page(template_values)
		
	
	def post(self):
		userid = self.request.cookies.get('user', False)
		images=data_source.products()
		
		if userid:
			path = self.request.get("path")
			p = db.Query(models.Product).filter("prod_url = ", path)
			q = p.get()
			
			data=models.Cart()
			data.userid = self.request.get("user")
			data.product = q.prod_title
			data.prod_manu = q.prod_manufacturer
			data.description = q.prod_overview
			data.path = path
			data.price = q.prod_price
			data.put()
			self.redirect(str(path))
			
		else:
			self.redirect(str(self.request.get("path")))
	
	
class ReviewsHandler(views.TempView):
	def post(self):
		product = self.request.get("product")
		form_url = self.request.get("url")
		familiarity = self.request.get("familiarity")
		purchase = self.request.get("purchase")
		rating = self.request.get("prod_rating")
		overall_rating = self.request.get("overall_rating")
		review_title = self.request.get("title")
		review = self.request.get("opinion")
		
		review_data = models.Reviews(product = product, familiarity = int(familiarity), purchase = int(purchase), rating = int(rating), overall_rating = int(overall_rating), review_title = review_title, review = review)
		review_data.put()
		self.redirect(str(form_url))
	
		
app = webapp2.WSGIApplication([('/products/reviews', ReviewsHandler),
                               ('/products/.*', ProductHandler)],
		                        debug=True)