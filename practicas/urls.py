"""practicas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from . import views #se coloca un punto para hacer referencia al directorio raiz.

""" Aca se registran o definen
todas las urls de la aplicacion o proyecto """

urlpatterns = [
    
    path('admin/', admin.site.urls),
    #se define como un string vacio para hacer referencia al inicio
    path('',views.index, name='index'),#se debe asociar una url por cada vista o funcion en el archivo views.py
    
    path('saludo/', views.saludo, name='Saludo'),
    path('renderizado/',views.Renderizado,name='renderizado'),
    path('productos/',views.ListarArticulos,name='productos'),
    path('archivosestaticos/',views.archivosestaticos,name='archivosestaticos'),
    path('usuarios/login',views.login,name='login')
    
    
]
