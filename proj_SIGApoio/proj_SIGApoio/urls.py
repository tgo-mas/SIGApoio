
# from django.contrib import admin
from django.urls import path
from app_SIGApoio import views

urlpatterns = [
    path('',views.home,name = "home"),
]
