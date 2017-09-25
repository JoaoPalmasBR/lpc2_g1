from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *

# Create your views here.
def listaAgenda(request):
    lista = Agenda.objects.all()
    retorno=''
    for agenda in lista:
        retorno += '<p>Agenda: {}</p>'.format(agenda.usuario, agenda.tipo)
        lista2 = agenda.compromissos.all()
        retorno += '<p>Comprimissos: <ul>'
        for c in lista2:
            retorno += '<li>{}, {}</li>'.format(c.nome, c.data)
        retorno += '</ul></p><hr>'
    return HttpResponse(retorno)

def get_agenda_byID(request,id):
    lista = Agenda.objects.filter(usuario_id=id)
    retorno=''
    for agenda in lista:
        if agenda.tipo=="PUBLICA":
            retorno += '<p>Agenda Publica: {}</p>'.format(agenda.usuario)
            lista2 = agenda.compromissos.all()
            retorno += '<p>Comprimissos: <ul>'
            for c in lista2:
                retorno += '<li>{}, {}</li>'.format(c.nome, c.data)
            retorno += '</ul></p><hr>'
    return HttpResponse(retorno)

'''
def listaFeriado(request):
    lista = AgendaInstitucional.objects.all()
    retorno=''
    for ai in lista:
        retorno += '<p>Agenda Institucional: </p>'
        lista2 = ai.feriados.all()
        retorno += '<p>Feriados: <ul>'
        for c in lista2:
            retorno += '<li>{}, {}</li>'.format(c.nome, c.data)
        retorno += '</ul></p><hr>'
    return HttpResponse(retorno)
'''