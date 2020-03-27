from django.forms import ModelForm
from .models import *

class BookForm(ModelForm) :
    class Meta :
        model = Book
        fields = '__all__'