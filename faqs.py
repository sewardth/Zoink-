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


class FaqHandler(views.TempView):
	def page(self, page, template_values):
		self.render(page, template_values)
	
	def get(self):
		template_values = {}
		self.page('faq.html',template_values)


class QuestionHandler(views.TempView):
	def get(self):
		url_map = data_source.faq()
		url = self.get_path()
		question = url_map[url][0]
		answer = url_map[url][1]
		template_values = {'question' :question, 'answer': answer}
		self.render('faq_holder.html', template_values)

		
		
app = webapp2.WSGIApplication([('/FAQs', FaqHandler), 
                               ('/FAQs/.*', QuestionHandler)],
		                        debug=True)