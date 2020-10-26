from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView
from .models import Product,Category
import datetime
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

class ProductFeaturedListView(ListView):
	template_name = "products/lists.html"

class ProductFeaturedDetailView(DetailView):

	queryset = Product.objects.all()
	template_name = "products/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()


class ProductListView(ListView):

	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}

	template_name = "products/list.html"


def product_list_view(request):
	# if 'gender' in request.GET:
	# 	queryset = Product.objects.filter(gender=request.GET.get('gender'))
	# queryset = Product.objects.all()
	dict_ = {i.category:i.product_set.all() for i in Category.objects.all()}

	context = { 'object_list' :dict_,'categories':Category.objects.all()}
	return render(request, "products/list.html", context)

def gender_views(request,gender):
	dict_ = {i.category:i.product_set.all().filter(gender=gender) for i in Category.objects.all()}

	context = { 'object_list' :dict_,'categories':Category.objects.all()}
	return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"


def get_queryset(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		return Product.objects.filter(pk=pk)



def product_detail_view(request, pk=None, *args, **kwargs):


	# #try:
	instance = Product.objects.get_by_id(pk)
	print(instance)
	if instance is None:
	 	raise Http404("Product doesn't exist")

	return render(request, "products/detail.html", context)

# This is the function to view cart.
@login_required
def view_cart(request):
	return render(request,'cart.html',{'products':request.user.cart})

# This executes when you add a item to cart.

@login_required
def add_to_cart(request,pk):
	# A simple try catch block so it doesn't show errors
	try:
		# This adds the product to cart.

		request.user.cart.add(Product.objects.get(pk=pk))
	except Product.DoesNotExist:
		pass
	return redirect('view_cart')

@login_required
def remove_from_cart(request,pk):
	# A simple try catch block so it doesn't show errors
	try:
		# This removes the product to cart.
		request.user.cart.remove(Product.objects.get(pk=pk))

	except Product.DoesNotExist:
		pass
	return redirect('view_cart')
