from django.contrib import admin
from django.contrib import Page

from .models import Item, OrderItem, Order, Page


# Register your models here.
admin.site.register(Page)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
