from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=50, unique=True, primary_key=True)

class Usuario(models.Model):
    matricula = models.IntegerField(primary_key=True, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    nome = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    #escala  = models.ForeignKey(Horario, on_delete=models.SET_NULL, default=None)
