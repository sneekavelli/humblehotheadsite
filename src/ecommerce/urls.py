"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.conf import settings
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *
from products.views import (
 ProductListView,
 product_list_view,
 ProductDetailView,
 #ProductDetailSlugView,
 product_detail_view,
 ProductFeaturedListView,
 ProductFeaturedDetailView,
 view_cart,
 add_to_cart
)

from .views import (
 	 home_page,
     contact_page,
     login_page,
     register_page

 	)
from django.contrib.auth import get_user_model




urlpatterns = [


    path('', home_page,name='home'),
    path('contact/', contact_page),
    path('login/', login_page),
    path('register/', register_page),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('featured-fbv', product_list_view),
    path('products/', ProductListView.as_view()),
    path( 'products-fbv/', product_list_view),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    #path('products/<str:slug>', ProductDetailSlugView.as_view()),
    path('products-fbv/<int:pk>/', product_detail_view),
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    path('user/cart/',view_cart,name='view_cart'),
    path('user/cart/add/<pk>/',add_to_cart,name='add_to_cart'),

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
