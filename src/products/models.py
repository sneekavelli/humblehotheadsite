import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save


# Create your models here.
def get_filename_ext(filename):
	base_name = os.path.basename(filename)
	name, ext = os.path.splitext(filename)
	return name, ext

def upload_image_path(instance, filename):
	print(instance)
	print(filename)
	new_filename = random.randint(1,3999991)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(
			new_filename= new_filename, 
			final_filename= final_filename
			)

class ProductQueryset(models.query.QuerySet):
	
	#def active(self):
	#	return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True)
class ProductManager(models.Manager):
	
	#def all(self):
	#	return self.get_queryset().active(featured=True)
	def featured(self):
		return self.get_queryset().filter(featured=True)
	def features(self):
		return self.get_queryset().filter.featued()
		
	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)
		return self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

class Product (models.Model):
	title 			= models.CharField(max_length=120)
	slug			= models.SlugField(blank=True)
	description 	= models.TextField()
	price			= models.DecimalField(decimal_places=2, max_digits=20)
	image 			= models.ImageField(upload_to= upload_image_path,null=True, blank=True,)
	objects 		= ProductManager()
	featured		= models.BooleanField(default=False)
	active			= models.BooleanField(default=True)

	objects = ProductManager

	def __str__(self):
		return self.title
	
	def __unicode__(self):
		return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver, sender = Product)

