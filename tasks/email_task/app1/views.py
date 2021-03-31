from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'app1/index.html',{})

def signup(request):
    registered = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True

        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request,'app1/signup.html',{'form':form,'registered':registered})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email,password=password)

        if user:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account not active")

        else:
            print("Invalid details")
            return redirect('login')

    else:
        return render(request,'app1/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
