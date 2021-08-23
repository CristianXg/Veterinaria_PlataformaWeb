from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('app.gestion_clientes.urls')),
    path('login/', include('app.login.urls')),
    path('', views.index, name='index'),
    
]
