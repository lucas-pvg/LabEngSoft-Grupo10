from django.db import models
import datetime

# Create your models here.
class Voo(models.Model):
    idVoo = models.IntegerField(primary_key=True)
    codigoVoo = models.IntegerField(max_length=100, null=False)
    companhiaAerea = models.CharField(max_length=100, null=False)
    partidaprevisao = models.DateTimeField(null=False)
    partidaOficial = models.DateTimeField(null=True)
    chegadaPrevisao = models.DateTimeField(null=False)
    chegadaOficial = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, null=False)
    rota = models.CharField(max_length=100, null=True)
    aeroportoOrigem = models.CharField(max_length=100, null=False)
    aeroportoDestino = models.CharField(max_length=100, null=False)
    class Meta:
        db_table = 'voos'


class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    cargo = models.CharField(max_length=100, null=False)
    companhiaAerea = models.CharField(max_length=100, null=False)
    aeroportoTrabalho = models.CharField(max_length=100, null=False)
    class Meta:
        db_table = 'usuarios'
