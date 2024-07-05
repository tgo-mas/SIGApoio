
from django.contrib import admin
from django.urls import path, include
from app_SIGApoio import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name = "home"),
    path('cad_local/',views.cad_local, name = "cad_local"),
    path('success_page/', views.success_page, name = "success_page"),
    path('admin/', admin.site.urls)
    path('admin/', admin.site.urls),
    path('', include('app_SIGApoio.urls'))
]