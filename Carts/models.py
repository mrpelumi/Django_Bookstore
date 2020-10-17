from django.db import models
from django.contrib.auth.models import User
from acubook.models import BookInfo,UserProfileInfo
# Create your models here.

class Cart(models.Model):
	currentuser = models.OneToOneField(UserProfileInfo,on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return "Cart name: %s" %(self.currentuser)

class CartItem(models.Model):
	cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
	book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	
	def price_subtotal(self):
		subtotal = self.book.Price * self.quantity
		return subtotal


	def __str__(self):
		return str(self.cart.currentuser)
	
#class Order(models.Model):
	#order_id = models.CharField()
	#user_cart = models.ForeignKey(Cart,on_delete=)