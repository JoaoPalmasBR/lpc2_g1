from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *

# Create your views here.
def listaAgenda(request):
    lista = Agenda.objects.all()
    retorno=''
    for agenda in lista:
        retorno += '<p>Agenda: {}</p><br>'.format(agenda.usuario, agenda.tipo)
        lista2 = agenda.compromissos.all()
        for c in lista2:
            retorno += '<p>{}</p>'.format(c.nome)
        retorno += '<hr>'
    return HttpResponse(retorno)