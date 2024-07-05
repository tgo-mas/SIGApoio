
from django.contrib import admin
from django.urls import path, include
from app_SIGApoio import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name = "home"),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)