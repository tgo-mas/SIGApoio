from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=50, unique=True, primary_key=True)

class Usuario(models.Model):
    matricula = models.IntegerField(primary_key=True, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    nome = models.CharField(max_length=200)
    tipo = models.OneToOneField(TipoUsuario, on_delete=models.CASCADE)
    #escala  = models.ForeignKey(Horario, on_delete=models.SET_NULL, default=None)

class TipoRecurso(models.Model):
    tipo = models.CharField(max_length=100)

class Recurso(models.Model):
    
    STATUS_CHOICE = ((True,"Disponível"),(False,"Indispovível"))
    FUNCIONANDO_CHOICE = ((True,"Sim"),(False,"Não"))
    
    codigo = models.IntegerField(primary_key=True, unique=True)
    tipo = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
    status = models.BooleanField(choices=STATUS_CHOICE, blank=True, default=True,)
    funcionando = models.BooleanField(choices=FUNCIONANDO_CHOICE, blank=True, default=True)

class Emprestimo(models.Model):
    horaSaida = models.DateTimeField(auto_now=True)
    horaEntrada = models.DateTimeField()
    idRecurso = models.ForeignKey(Recurso, on_delete=models.DO_NOTHING)
    matBolsista = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING) 
    matUsuario = models.ForeignKey(Usuario, related_name='%(class)s_usuario', on_delete=models.DO_NOTHING, default='')


class Sala(models.Model):
    bloco = models.CharField(max_length=1)
    
