
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('get_locais/', views.getLocais, name = "getLocais"),
    path('success_page/', views.success_page, name = "success_page")
]
