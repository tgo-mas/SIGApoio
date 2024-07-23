
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('get_locais/', views.getLocais, name = "getLocais"),
    path('success_page/', views.success_page, name = "success_page")
]
