from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from account.form import AccountCreationForm

# Create your views here.

def loginuser(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return(redirect('store'))
        else :
            messages.info(request, 'Username OR Password is incorrect')
    return(render(request, 'user_login/login.html'))

def logoutuser(request) :
    logout(request)
    return(redirect('login'))

def registeruser(request) :
    form = AccountCreationForm()
    if request.method == 'POST' :
        form = AccountCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            return(redirect('login'))
            messages.info(request, 'User was created successfully')
    context = {'form':form}
    return(render(request, 'user_login/register.html', context))