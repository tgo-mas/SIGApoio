
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name = "home"),
    path('cadastro_recurso',views.cadastroRecurso, name= "cad_recurso"),
    path('cad_local/',views.cad_local, name = "cad_local"),
    path('reserva/cadastro',views.cadastroReserva, name = "cad_reserva"),
    path('get_locais/', views.getLocais, name = "getLocais"),
    path('success_page/', views.success_page, name = "success_page"),
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
    ]