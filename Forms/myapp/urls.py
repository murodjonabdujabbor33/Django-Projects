from django.urls import path
from .views import register, main

urlpatterns = [
    path('reg/', register, name='home'),
    path('', main, name='main'),
]