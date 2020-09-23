import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save

from django.utils.text import slugify
from django.utils.crypto import get_random_string


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

class Category(models.Model):
	category = models.CharField(max_length=50,unique=True)
	def __str__(self):
		return self.category

class Product (models.Model):
	title 			= models.CharField(max_length=120)
	slug			= models.SlugField(blank=True)
	description 	= models.TextField()
	price			= models.DecimalField(decimal_places=2, max_digits=20)
	image 			= models.ImageField(upload_to= upload_image_path,null=True, blank=True,)
	objects 		= ProductManager()
	featured		= models.BooleanField(default=False)
	active			= models.BooleanField(default=True)
	category 		= models.ForeignKey(to=Category,on_delete=models.CASCADE)

	objects = ProductManager

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

	# Below code will check if there exists a same slug.
	# If so then it'll add random_string so it's unique

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
		# If same slug exists then append a random string of 4 characters( you can choose length accordingly ).
		# then it returns unique_slug_generator again(recursion) to check if new_slug exists or not.
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=get_random_string(length=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender = Product)
