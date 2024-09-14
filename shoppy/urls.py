from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoppypage, name='shoppy'),
]