"""Libro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from libroseguro import views

urlpatterns = [

    url('lista_libro/',views.listar_libro,name='Lista_libro'),
    url('crea_libro/',views.crear_libro,name='crea_libro'),
    url('editar_libro/<int:id>',views.editar_libro,name='edita_libro'),
    url('crea_libro/<int:id>',views.eliminar_libro,name='elimina_libro'),
    path('admin/', admin.site.urls),

]
