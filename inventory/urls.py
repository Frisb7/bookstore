from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log/', views.log, name='log'),
    path('add/', views.add_book, name='add'),
    path('update/<str:pk>/', views.update_book, name='update'),
    path('delete/<str:pk>/', views.delete_book, name='delete'),
]