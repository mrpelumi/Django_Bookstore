from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfileInfo(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)

	#additional fields
	def __str__(self):
		return str(self.user)

def create_user_profile(sender,instance,created,**kwargs):
	if created:
		UserProfileInfo.objects.create(user=instance)
post_save.connect(create_user_profile,sender=User) 

	

class Category(models.Model):
	categories = [
		('Arts and Literature','Arts and Literature'),
		('Science','Science'),
		('Christian Books','Christian Books'),
		('Nigerian and African Authors','Nigerian and African Authors'),
		('Motivational','Motivational'),
		('Business','Business'),
		('Teen Books','Teen Books')
	]
	categorys = models.CharField(max_length=256,choices=categories,default='Arts and Literature')

	def __str__(self):
		return str(self.categorys)

class BookInfo(models.Model):
	Book_image = models.ImageField(null=True,blank=True)
	Title = models.CharField(max_length=265,unique=True)
	Authors = models.CharField(max_length=256)
	Publish_year = models.IntegerField()
	Price = models.IntegerField()
	Description = models.TextField()
	Quantity = models.IntegerField(default=1)
	bookcategories = models.ManyToManyField(Category)


	def __str__(self):
		return self.Title

