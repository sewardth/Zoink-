import webapp2
import views
import data_source
from google.appengine.ext import db

# main.py script
class SignUp(db.Model):
	first_name = db.StringProperty(required = True)
	last_name = db.StringProperty(required = True)
	email_address = db.EmailProperty(required = True)
	sign_date = db.DateTimeProperty(auto_now_add = True)
	approved = db.IntegerProperty(default = 0)
	active = db.IntegerProperty(default =0)
	activation_url = db.StringProperty()
	
# pages.py script
class Contact(db.Model):
	name = db.StringProperty(required = True)
	email_address = db.EmailProperty(required = True)
	response = db.TextProperty(required = True)
	submission_date = db.DateTimeProperty(auto_now_add = True)

class Suggestions(db.Model):
	name = db.StringProperty(required = True)
	email_address = db.EmailProperty(required = True)
	gadget_name = db.StringProperty(required = True)
	gadget_url = db.LinkProperty(required = True)
	rental_price = db.FloatProperty(required = True)
	submission_date = db.DateTimeProperty(auto_now_add = True)
	
class Partnerships(db.Model):
	name = db.StringProperty(required = True)
	company = db.StringProperty(required = True)
	email = db.EmailProperty(required = True)
	phone = db.PhoneNumberProperty(required = True)
	submission_date = db.DateTimeProperty(auto_now_add = True)
	
# products.py script
class Reviews(db.Model):
	product = db.StringProperty(required = True)
	familiarity = db.IntegerProperty(required = True)
	purchase = db.IntegerProperty(required = True)
	rating = db.IntegerProperty(required =True)
	overall_rating = db.IntegerProperty(required = True)
	review_title = db.StringProperty()
	review = db.TextProperty()
	complete_time = db.DateTimeProperty(auto_now_add = True)
	
class Cart(db.Model):
	userid = db.StringProperty()
	product = db.StringProperty()
	prod_manu = db.StringProperty()
	description = db.TextProperty()
	path = db.StringProperty()
	price = db.FloatProperty()
	add_time = db.DateTimeProperty(auto_now_add = True)
	
# admin.py script
class Product(db.Model):
	prod_url = db.StringProperty()
	prod_title = db.StringProperty()
	prod_manufacturer = db.StringProperty()
	prod_price = db.FloatProperty()
	starting_inventory = db.IntegerProperty()
	youtube = db.LinkProperty()
	image_large = db.BlobProperty()
	image_normal = db.BlobProperty()
	image_thumb = db.BlobProperty()
	zoink_perspective = db.TextProperty()	
	prod_overview = db.TextProperty()	
	need_to_know = db.TextProperty()	
	date = db.DateTimeProperty(auto_now_add = True)
	active = db.IntegerProperty (default = 1)
	
#Users
class Users(db.Model):
	user_email =db.EmailProperty()
	password = db.StringProperty()
	first_name = db.StringProperty()
	last_name = db.StringProperty()
	activation_date = db.DateTimeProperty(auto_now_add = True)
	currently_active = db.IntegerProperty (default=1)
	session_key = db.StringProperty()
	salt = db.StringProperty()
	
#Checkout
class Checkout(db.Model):
	userid = db.StringProperty()
	billing_first_name = db.StringProperty()
	billing_last_name = db.StringProperty()
	billing_street_address = db.StringProperty()
	billing_extended_address = db.StringProperty()
	billing_city = db.StringProperty()
	billing_state = db.StringProperty()
	billing_postalCode = db.StringProperty()
	shipping_first_name = db.StringProperty()
	shipping_last_name = db.StringProperty()
	shipping_street_address = db.StringProperty()
	shipping_extended_address = db.StringProperty()
	shipping_city = db.StringProperty()
	shipping_state = db.StringProperty()
	shipping_postalCode = db.StringProperty()
	braintree_trans_id = db.StringProperty()
	product = db.StringProperty()
	product_price = db.FloatProperty()
	transaction_date = db.DateTimeProperty(auto_now_add = True)