from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import Form,LoginForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        user_form = Form(request.POST,request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            login(request,user)

            return redirect('home')
        else:
            return render(request,'auth/register.html',{'user_form':user_form,})

    else:
        user_form = Form()
    return render(request,'auth/register.html',{'user_form':user_form,})

def login_(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,email=form.cleaned_data['email'],password=form.cleaned_data['password'])
            print(CustomUser.objects.get(email=form.cleaned_data['email']))
            if user:
                login(request,user)
                return redirect('home')
        return render(request,'auth/login.html',{'form':form,'error':'Invalid email and/or password'})
    return render(request,'auth/login.html',{'form':form})


def logout_(request):
    logout(request)
    return redirect('home')
