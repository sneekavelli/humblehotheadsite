from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView
from .models import Product,Category
import datetime
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

class ProductFeaturedListView(ListView):
	template_name = "products/lists.html"

#	def get_queryset(self, *args, **kwargs):
#		request = self.request
#		return Product.objects.featured()

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
	queryset = Product.objects.all()
	if 'category' in request.GET:
		cats = request.GET.get('category').split(',')
		cats = list(map(lambda x:int(x),cats))
		queryset = Product.objects.filter(category__pk__in=cats)
	if 'gender' in request.GET:
		queryset = Product.objects.filter(gender=request.GET.get('gender'))

	context = { 'object_list' :queryset,'categories':Category.objects.all()}
	return render(request, "products/list.html", context)


#class ProductDetailSlugView(DetailView):
#	queryset = Product.objects.all()
#	template_name = "products/detail.html"


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"


	#  def get_context_data(self, *args, **kwargs):
	#  	context = super(ProductDetailView, self).get_context_data(*args **kwargs)
	#  	print(context)
	#  	return context

# def get_object(self, *args, **kwargs):
# 	request = self.request
# 	pk = self.kwargs.get('pk')
# 	instance = Product.objects.get_by_id(pk)
# 	if instance is None:
# 	 	raise Http404("Product doesn't exist")
# 	return instance

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

@login_required
def view_cart(request):
	print(request.user.cart.all())
	return render(request,'cart.html',{'products':request.user.cart})

@login_required
def add_to_cart(request,pk):
	try:
		request.user.cart.add(Product.objects.get(pk=pk))

	except Product.DoesNotExist:
		pass
	return redirect('view_cart')
