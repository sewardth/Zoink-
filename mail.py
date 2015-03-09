from google.appengine.api import mail

class ContactMailer():
	def customer_email(self,name, email):
		message = mail.EmailMessage(sender="Zoink.com Support <tseward@zoinktechrentals.com>",
		                            subject="Thank you for contacting us!")

		message.to = email

		message.body = """
		Dear %s:

		Thank you for contacting Zoink!.  One of our staff members will be in contact with you
		shortly.  In the mean time, please view our FAQs page if you have any questions.
		
		Thank you!

		The Zoink.com Team
		""" %(name)

		message.html = """
		<html><head></head><body>
		Dear %s:

		Thank you for contacting Zoink!.  One of our staff members will be in contact with you
		shortly.  In the mean time, please view our FAQs page if you have any questions.
		
		Thank you!

		The Zoink.com Team
		
		
		</body></html>
		"""%(name)

		message.send()
		
	def staff_email(self,name, email, response):
		message = mail.EmailMessage(sender="Zoink.com Support <tseward@zoinktechrentals.com>",
		                            subject="%s - New Contact Request" %(name))

		message.to = 'tseward@zoinktechrentals.com'

		message.body = """
		A new contact submission from %s via %s.
		
		Message:
		%s

		""" % (name, email, response)
		message.send()
		
class SignUpMailer():
	def email_response(self,first_name, email_address):
		message = mail.EmailMessage(sender="Zoink!.com Support <tseward@zoinktechrentals.com>",
			                            subject="Thank you for signing up with Zoink!")

		message.to = email_address

		message.body = """
			Dear %s:

			Thank you for signing up with Zoink!  Currently, we are operating in
			our beta phase, so we are approving accounts as our inventory grows.
			We will send you an email as soon as your account is ready for activation.
			
		    We thank you for your patience, and appologize for a delay in being
			able to rent from our awesome selection. In the mean time, please look 
			around our site to view current and future rental products and Zoink! updates. 

			Please let us know if you have any questions.

			The Zoink!.com Team
			""" %(first_name)

		message.html = """
			<html><head></head><body>
			Dear %s:

			Thank you for signing up with Zoink!  Currently, we are operating in
			our beta phase, so we are approving accounts as our inventory grows.
			We will send you an email as soon as your account is ready for activation.

			We thank you for your patience, and appologize for a delay in being
			able to rent from our awesome selection. In the mean time, please look 
			around our site to view current and future rental products and Zoink! updates. 

		  	Please let us know if you have any questions.

			The Zoink!.com Team
			
			
			</body></html>
			"""%(first_name)

		message.send()
			
			
class ApprovedMailer():
	def account_email(self,first_name, last_name, email, activation_link):
		message = mail.EmailMessage(sender="Zoink.com Accounts <tseward@zoinktechrentals.com>",
		                            subject="Your Zoink! Account is ready to be activated!")

		message.to = email

		message.body = """
		Hello, %s %s,
		Your Zoink! account is ready for activation!  Please click on the link below to get started.
		
		Account Link:
		%s
		
		Please contact our support team if you have questions.  Thank you!

		""" % (first_name, last_name, activation_link)
		message.send()