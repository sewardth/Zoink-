import braintree
import webapp2
import views
from google.appengine.ext import db
import models
from google.appengine.api import images



class paymentHandler(views.TempView):
	def get(self):
		userid = self.request.cookies.get('user', False)
		p = models.Cart.all()
		p = db.Query(models.Cart).filter("userid = ", userid)
		cart_products = p.fetch(100)
		total=[]
		for x in cart_products:
			total.append(x.price)
			
		
		template_values ={'products': cart_products,
						  'userid': userid,
						  'check_total': '%.2f' %sum(total)}
		
		self.render('checkout.html', template_values)
	
	def post(self):
		#Sandbox Code
		braintree.Configuration.configure(
		    braintree.Environment.Sandbox,
		    "jczbm7ymrk9zy54w",
		    "f5ss274cj6dpjytz",
		    "f984631554d7572720c6bf201aa59af4"
		)
		
		userid = self.request.cookies.get('user', False)
		query = db.Query(models.Users).filter("user_email = ", userid)
		q = query.get()
		
		user_id = q.key().id()
		
		p = db.Query(models.Cart).filter("userid = ", userid)
		cart_products = p.fetch(100)
		total=[]
		for x in cart_products:
			total.append(x.price)
		
		
		result = braintree.Transaction.sale({
		    "amount":str(round(sum(total),2)),
		    "customer": {
				#"id": user_id,
		        "first_name": self.request.get("first_name"),
		        "last_name": self.request.get("last_name"),
				"email": userid
		    },
		    "credit_card": {
		        "number": self.request.get("number"),
				"cvv": self.request.get("cvv"),
				"expiration_month": self.request.get("month"),
			    "expiration_year": self.request.get("year")
		    },
		    "billing": {
		        "street_address": self.request.get("street_address"),
				"extended_address" : self.request.get("extended_address"),
		        "locality": self.request.get("ship_locality"),
		        "region": self.request.get("ship_region"),
		        "postal_code": self.request.get("ship_postal_code"),
				"country_code_alpha2": "US"
		    },
		    "options": {
		        "store_in_vault": False,
		        "add_billing_address_to_payment_method": True,
				"submit_for_settlement": True
		    }
		})

		if result.is_success:
			
			for x in cart_products:
				c = models.Checkout()
				c.product = x.product
				c.product_price = x.price
				c.userid = userid
				c.billing_first_name = self.request.get("first_name")
				c.billing_last_name = self.request.get("last_name")
				c.billing_street_address = self.request.get("street_address")
				c.billing_extended_address = self.request.get("extended_address")
				c.billing_city = self.request.get("locality")
				c.billing_state = self.request.get("region")
				c.billing_postalCode = self.request.get("postal_code")
				c.braintree_trans_id = result.transaction.id
				
				#Statement not currently working correctly
				if self.request.get("ship_street_address") != self.request.get("street_address"):
					c.shipping_first_name = c.billing_first_name
					c.shipping_last_name = c.billing_last_name
					c.shipping_street_address = c.billing_street_address
					c.shipping_extended_address = c.billing_extended_address
					c.shipping_city = c.billing_city
					c.shipping_state = c.billing_state
					c.shipping_postalCode = c.billing_postalCode

				else:
					c.shipping_first_name = self.request.get("ship_first_name")
					c.shipping_last_name = self.request.get("ship_last_name")
					c.shipping_street_address = self.request.get("ship_street_address")
					c.shipping_extended_address = self.request.get("ship_extended_address")
					c.shipping_city = self.request.get("ship_locality")	
					c.shipping_state = self.request.get("ship_region")
					c.shipping_postalCode = self.request.get("ship_postal_code")
				c.put()
			
			for x in cart_products:
				db.delete(x)
				
			self.response.out.write("success!: " + result.transaction.id)
		
		elif result.transaction:
		    self.response.out.write("Error processing transaction:")
		    self.response.out.write("  message: " + result.message)
		    self.response.out.write("  code:    " + result.transaction.processor_response_code)
		    self.response.out.write("  text:    " + result.transaction.processor_response_text)
		else:
		    self.response.out.write("message: " + result.message)
		    for error in result.errors.deep_errors:
		        self.response.out.write("attribute: " + error.attribute)
		        self.response.out.write("  code: " + error.code)
		        self.response.out.write("  message: " + error.message)
		
app = webapp2.WSGIApplication([('/checkout', paymentHandler)],
								debug=True)
