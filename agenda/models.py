from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    def __str__(self):
        return "{}".format(self.nome)
class Compromisso(models.Model):
    nome = models.CharField(max_length=128, null=True, blank=False)
    data = models.DateField(blank=True, null=True)
    def __str__(self):
        return "{} - {}".format(self.nome,self.data)
class AgendaInstitucional(models.Model):
    feriados = models.ManyToManyField(Compromisso)
class Agenda(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=False)
    tipos = (
        (u'PRIVADA',u'PRIVADA'),
        (u'PUBLICA',u'PUBLICA'),
    )
    tipo=models.CharField(max_length=7, choices=tipos)
    compromissos = models.ManyToManyField(Compromisso, verbose_name="compromissos")