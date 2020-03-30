from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from account.form import AccountCreationForm
from account.models import Account
from django.http import HttpResponseRedirect

# Create your views here.

def loginuser(request) :
    if request.method == 'POST' :
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None :
            login(request, user)
            return(redirect('store'))
        else :
            context = {'email':email}
            messages.info(request, 'Email OR Password is incorrect')
            return(render(request, 'user_login/login_cont.html', context))
    return(render(request, 'user_login/login.html'))

def logoutuser(request) :
    logout(request)
    return(redirect('login'))

def registeruser(request) :
    form = AccountCreationForm()
    if request.method == 'POST' :
        form = AccountCreationForm(request.POST)
        current = request.POST
        if form.is_valid() :
            form.save()
            messages.info(request, 'User was created successfully')
            email = current['email']
            context = {'email':email}
            return(render(request, 'user_login/login_cont.html', context))
        else :
            account = Account.objects.all().values('email', 'username', 'first_name', 'last_name', 'grno')
            for i in account :
                if i['email'] == current['email'] :
                    messages.info(request, 'A account already exists with this Email')
                    break
                if i['username'] == current['username'] :
                    messages.info(request, 'A account already exists with this Username')
                    break
                if i['grno'] == current['grno'] :
                    messages.info(request, 'A account already exists with this Grno')
                    break
            if current['password1'] == current['password2'] :
                if len(current['password1']) < 8 :
                    messages.info(request, 'Password must be 8 characters long')
            else :
                messages.info(request, 'Confirm password doesnt match the original')
            context = {'form':form}
            return(render(request, 'user_login/register_cont.html', context))
    context = {'form':form}
    return(render(request, 'user_login/register.html', context))