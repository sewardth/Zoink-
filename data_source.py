#!/usr/bin/env python

def faq():
	url_map = {'/FAQs/what-is-zoink':('What is Zoink!?', 'Response'),
	'/FAQs/how-does-zoink-work': ('How Does Zoink! Work?', 'Response'),
	'/FAQs/how-can-i-provide-feedback-to-zoink': ('How can I provide feedback to Zoink!?', 'Response'),
	'/FAQs/when-will-my-gadget-arrive': ('When will my gadget arrive?', 'Response'),
	'/FAQs/how-long-can-i-rent-a-gadget-for': ('How long can I rent a gadget for?','Response'),
	'/FAQs/when-do-i-ship-my-gadget-back': ('When do I ship my gadget back?','Response'),
	'/FAQs/how-do-i-mail-my-gadget-back': ('How do I mail my gadget back?','Response'),
	'/FAQs/i-lost-my-shipping-info': ('Help, I lost my return shipping box and label.  What should I do?','Response'),
	'/FAQs/what-happens-if-i-mail-my-gadget-back-late': ('What happens if I mail my gadget back late?','Response'),
	'/FAQs/can-i-suggest-an-item-for-zoink-to-carry': ('Can I suggest an item for Zoink! to carry?','Response'),
	'/FAQs/will-zoink-rent-out-my-companys-gadgets': ("Will Zoink! rent out my company's gadgets?",'Response'),
	'/FAQs/i-left-sensitive-information-on-my-gadget': ('I left sensitive information on my gadget, will you remove it?', 'Response'),
	'/FAQs/what-happens-to-the-apps-i-downloaded-on-my-rental': ('What happens to the apps I paid for and downloaded onto my rental gadget?', 'Response'),
	'/FAQs/what-if-i-want-to-keep-my-item-longer-than-my-paid-time-period': ('What if I want to keep my item longer than my paid time period?', 'Response'),
	'/FAQs/can-i-buy-the-item-after-i-rent-it': ('What if I love the gadget and want to keep it? Can I buy it?', 'Response'),
	'/FAQs/how-do-i-provide-a-rating-for-my-gadget': ('How do I provide a rating for my gadget?', 'Response'),
	'/FAQs/who-does-zoink-like-to-partner-with': ('Who does Zoink! like to partner with?','Response'),
	'/FAQs/can-zoink-provide-my-company-with-feedback-about-our-gadget': ('Can Zoink! provide my company with feedback about our gadget?', 'Response')}
	
	return url_map
	
def products():
	url_map = {'/products/Sphero': '../images/sphero-big.png',
	'/products/iPad-Mini': '../images/ipad-mini---large.png',
	'/products/Lytro-8GB-Camera': '../images/Lytro-Big.png'}
	
	return url_map



if __name__ == "__main__":
    pass