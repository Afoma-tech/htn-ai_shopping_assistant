from django.urls import path
from . import views

urlpatterns = [
    path('shoppy/', views.members, name='shoppy'),
]