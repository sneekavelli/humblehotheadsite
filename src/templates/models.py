from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


#class Page(models.Model):
#	title = models.Charfield(max_length=12, unique=True)
#	permalink = models.CharField(max_length=12, unique=True)
#	update_date = models.DateTimeField('Last Updated')
#	bodytext = model.TextField('Page Content', blank=True)


#	def __str__(self):
#		return self.title

class Product (models.Model):
	title 			= models.CharField(max_length=120)
	description 	= models.TextField()
	price			= models.DecimalField(decimal_places=2, max_digits=20)
	image 			= models.FileField(upload_to='products/', null=True, blank=True)

	def __str__(self):
		return self.title
	
	def __unicode__(self):
		return self.title



class Images(models.Model):
	photo = models.Imagefield()

	class Meta
		verbose_name_plural = "Images"

	def __str__(self):
		return self.photo.name
