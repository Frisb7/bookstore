from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginuser(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return(redirect('inventory'))
        else :
            messages.info(request, 'Username OR Password is incorrect')
    return(render(request, 'user_login/login.html'))

def logoutuser(request) :
    logout(request)
    return(redirect('login'))