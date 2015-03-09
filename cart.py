import webapp2
import data_source
import views
from google.appengine.ext import db
import models
import urllib



class cartviewer(views.TempView):
	def get(self):
		userid = self.request.cookies.get('user', False)
		p = db.Query(models.Cart).filter("userid = ", userid)
		cart_products = p.fetch(100)
		total=[]
		for x in cart_products:
			total.append(x.price)
			
		
		template_values ={'products': cart_products,
						  'userid': userid,
						  'check_total': '%.2f' %sum(total)}
		
		self.render('cart.html', template_values)

	def post(self):
		row_id = int(self.request.get("row"))
		row = models.Cart.get_by_id(row_id)
		db.delete(row)
		self.redirect("/cart")

app = webapp2.WSGIApplication([('/cart', cartviewer)],
		                        debug=True)