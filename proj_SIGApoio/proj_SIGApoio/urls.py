
from django.contrib import admin
from django.urls import path, include
from app_SIGApoio import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('cad_page/',views.cad_page, name = "cad_page"),
    path('admin/', admin.site.urls)
]

