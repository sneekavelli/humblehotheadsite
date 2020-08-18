from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import (ContactForm, LoginForm, RegisterForm)
import random
from django.shortcuts import redirect


def home_page(request):
	context ={
	"title": "THE OFFICIAL HUMBLE HOTHEADS WEBSITE",
	"content": "Welcome to the home page",
	'n': random.random()
	}
	if request.user.is_authenticated:
	    	
	    context["premium_content"] = "YEAHH"
		
	return render(request, 'home_page.html' , context)
		


def login_page(request):
    form = LoginForm(request.POST or None)
    context= {
    	"form": form
    }
    print("User logged in")
    if form.is_valid():
    	username = form.cleaned_data.get("username")
    	password = form.cleaned_data.get("password")
    	user = authenticate(request, username =username, password=password)
    	print(user)
    	if user is not None:
    		login(request, user)
    
    		return redirect("/home")
    	else:
    		ptint("Error")
		

    return render(request, "auth/login.html", context)	

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home_page.html')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
	"title": "Welcome to our contact page",
	"content": "Please fill in your details to get our latest drops",
	"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data )
	#if request.method == "POST" :
		# print (request.POST) 
		# print (request.POST.get('fullname'))
		# print (request.POST.get('email'))
		# print (request.POST.get('content'))
		return render(request, "contact/view.html", context)

#def about(request):
#	time = datetime.datetime.now()
#	return render(request, 'about.html', {'time':time})




	





