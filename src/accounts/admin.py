from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.



class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),)

    add_fieldsets = (
        (None, {
            'fields': ('email','first_name','last_name','password1', 'password2','profile_pic','portfolio_site'),}),)


admin.site.register(CustomUser,CustomUserAdmin)
