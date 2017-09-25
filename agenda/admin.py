from django.contrib import admin
from agenda.models import *
# Register your models here.
admin.site.register(Usuario)

admin.site.register(Agenda)
admin.site.register(Compromisso)
admin.site.register(Convite)