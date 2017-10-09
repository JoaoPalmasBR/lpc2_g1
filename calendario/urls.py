"""calendario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from agenda.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'agendas', AgendaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    #url(r'^agendas/$', listaAgenda),
    #url(r'^agendas/usuario/(?P<id>[0-9]{1})/', get_agenda_byID),
    #url(r'^agendas/feriados/$', listaFeriado),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]
