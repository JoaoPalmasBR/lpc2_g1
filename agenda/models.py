from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    def __str__(self):
        return "{}".format(self.nome)
class Agenda(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, blank=False)
    institucional = models.BooleanField(default=False)
    tipos = (
        (u'PUBLICA',u'PUBLICA'),
        (u'PRIVADA',u'PRIVADA'),
    )
    tipo=models.CharField(max_length=7, choices=tipos)
    permitidos = models.ManyToManyField(Usuario, null=True, blank=False, related_name="usuariospermitidosveragenda")
    def __str__(self):
        return "{} - (Institucional: {}) - {}".format(self.usuario, self.institucional, self. tipo)
class Compromisso(models.Model):
    nome = models.CharField(max_length=128, null=True, blank=False)
    dhinicio = models.DateTimeField(blank=True, null=True)
    dhfim = models.DateTimeField(blank=True, null=True)
    agenda = models.ForeignKey(Agenda, null=True, blank=False)
    convidados = models.ManyToManyField(Usuario, null=True, blank=False, related_name="usuariosconvidadosparacompromisso")
    def __str__(self):
        return "{} - ({} _ {}) {}".format(self.nome, self.dhinicio,self.dhfim,self.agenda)

class Convite(models.Model):
    sender = models.ForeignKey(Usuario, null=True, blank=False, related_name="Sender")
    receiver = models.ForeignKey(Usuario, null=True, blank=False, related_name="Receiver")
    compromisso = models.ForeignKey(Compromisso, null=True, blank=False, related_name="Compromisso")
    answer = models.BooleanField(default=False, verbose_name="Resposta")
    def __str__(self):
        return "{} convida {} para {} que diz: {}".format(self.sender,self.receiver,self.compromisso, self.answer)