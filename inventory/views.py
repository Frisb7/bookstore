from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def inventory(request) :
    books = Book.objects.all()
    context = {'books':books}
    return(render(request, 'inventory/home.html', context))

@login_required(login_url='login')
def add_book(request) :
    form = BookForm()
    if request.method == 'POST' :
        form = BookForm(request.POST)
        if form.is_valid() :
            form.save()
            return(redirect('/inventory/'))
    context = {'form':form}
    return(render(request, 'inventory/add_book.html', context))

@login_required(login_url='login')
def update_book(request, pk) :
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST' :
        form = BookForm(request.POST, instance=book)
        if form.is_valid() :
            form.save()
            return(redirect('/inventory/'))
    context = {'form':form}
    return(render(request, 'inventory/update_book.html', context))

@login_required(login_url='login')
def delete_book(request, pk) :
    book = Book.objects.get(id=pk)
    if request.method == 'POST' :
        book.delete()
        return(redirect('/inventory/'))
    context = {'book':book}
    return(render(request, 'inventory/delete_book.html', context))

# @login_required(login_url='login')
# def log(request) :
#     logs = Log.objects.all()
#     context = {'logs':logs}
#     return(render(request, 'inventory/log.html', context))