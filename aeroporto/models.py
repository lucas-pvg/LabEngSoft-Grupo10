from django.db import models
from django.urls import reverse

# Create your models here.
class Voo(models.Model):
    idVoo = models.IntegerField(primary_key=True, unique=True)
    codigoVoo = models.IntegerField(max_length=100, null=False, unique=True)
    companhiaAerea = models.CharField(max_length=100, null=False)
    partidaPrevista = models.DateTimeField(null=False)
    partidaReal = models.DateTimeField(null=True)
    chegadaPrevista = models.DateTimeField(null=False)
    chegadaReal = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, null=False)
    rota = models.CharField(max_length=100, null=True)
    aeroportoOrigem = models.CharField(max_length=100, null=False)
    aeroportoDestino = models.CharField(max_length=100, null=False)
    class Meta:
        db_table = 'voos'
        
    def get_absolute_url(self):
        return reverse('crud')
    


class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, unique=True)
    nome = models.CharField(max_length=100, null=False)
    cargo = models.CharField(max_length=100, null=False)
    companhiaAerea = models.CharField(max_length=100, null=True)
    aeroportoTrabalho = models.CharField(max_length=100, null=False)
    class Meta:
        db_table = 'usuarios'
