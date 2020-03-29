from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventory.models import Book

# Create your views here.

@login_required(login_url='login')
def store(request) :
    books = Book.objects.all()
    context = {'books':books}
    return(render(request, 'store/store.html', context))