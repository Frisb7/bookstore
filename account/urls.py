from django.urls import path
from . import views

urlpatterns = [
    path('unauth/', views.unauth, name='unauth'),
]