from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<str:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_from_cart2/<str:pk>/', views.remove_from_cart2, name='remove_from_cart2'),
    path('cart/receipt/', views.receipt, name='receipt'),
]