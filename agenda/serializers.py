from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from agenda.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email', 'is_staff')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome',)

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agenda
        fields = ('usuario','institucional','tipo','permitidos')