from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('api/v1/items/', views.createItem, name='createItem'),
    path(r'^api/v1/items/<str:item>/', views.item, name='item')
]