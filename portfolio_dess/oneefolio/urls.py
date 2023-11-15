from django import urls
from django.contrib import admin
from django.urls import include, path,re_path
from . import views

urlpatterns = [
    path('user_feedback/', views.emailView, name='email'),
]