from django.db import models
from datetime import date
from django.utils import timezone

class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=50, unique=True, primary_key=True)
    
    def __str__(self):
        return self.tipo


class Usuario(models.Model):
    matricula = models.IntegerField(primary_key=True, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    nome = models.CharField(max_length=200)
    tipo = models.OneToOneField(TipoUsuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.matricula} - {self.nome}'   # Mudei para retornar o número da matrícula

class TipoRecurso(models.Model):
    tipo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo

class Recurso(models.Model):
    
    STATUS_CHOICE = ((True,"Disponível"),(False,"Indispovível"))
    FUNCIONANDO_CHOICE = ((True,"Sim"),(False,"Não"))
    
    id_codigo = models.IntegerField(primary_key=True, unique=True)
    codigo = models.IntegerField(blank=True)
    tipo = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
    status = models.BooleanField(choices=STATUS_CHOICE, blank=True, default=True,)
    funcionando = models.BooleanField(choices=FUNCIONANDO_CHOICE, blank=True, default=True)
    
    def __str__(self):
        return self.tipo.tipo + ' ' + str(self.codigo)

class Emprestimo(models.Model):
    horaSaida = models.DateTimeField(default=timezone.now)  # Define a horaSaida como o momento atual quando o empréstimo é criado
    horaEntrada = models.DateTimeField(null=True, blank=True)  # Será preenchido ao registrar a devolução
    idRecurso = models.ForeignKey(Recurso, on_delete=models.DO_NOTHING)
    matBolsista = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    matUsuario = models.ForeignKey(Usuario, related_name='%(class)s_usuario', on_delete=models.DO_NOTHING, default='')
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.idRecurso.tipo.tipo} {self.idRecurso.codigo}"

    def registrar_devolucao(self):
        self.horaEntrada = timezone.now()  # Define a horaEntrada como o momento atual ao registrar a devolução
        self.devolvido = True
        self.save()

class Horario(models.Model): 
    SEMANA = ((0, 'Domingo'), (1, 'Segunda'), (2,'Terça'), (3, 'Quarta'), (4, 'Quinta'), (5, 'Sexta'), (6, 'Sábado'))

    id = models.CharField(max_length=3, default='2M1', primary_key=True)
    dia = models.IntegerField(choices=SEMANA, default=True)
    horaInicio = models.TimeField(null=True, blank=True)
    horaFim = models.TimeField(null=True, blank=True)
        
class TipoLocal(models.Model):
    tipo = models.CharField(max_length=50, unique=True, primary_key=True)
    
    def __str__(self):
        return self.tipo

class Local(models.Model):   
    nome = models.CharField(max_length=50, unique=True)
    bloco = models.CharField(max_length=10)
    capacidade = models.IntegerField()
    tipo = models.ForeignKey(TipoLocal, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nome
    
class ReservaSemanal(models.Model):    
    descricao = models.CharField(max_length=100, null=True)
    horarios = models.ManyToManyField(Horario) 
    local = models.ForeignKey(Local, on_delete=models.DO_NOTHING)
    matResponsavel = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING) 
    matSolicitante = models.ForeignKey(Usuario, related_name='%(class)s_usuario', on_delete=models.DO_NOTHING, default='')
    
class ReservaDiaUnico(models.Model):
    descricao = models.CharField(max_length=100, null=True)
    local = models.ForeignKey(Local, on_delete=models.DO_NOTHING)
    matResponsavel = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING) 
    matSolicitante = models.ForeignKey(Usuario, related_name='%(class)s_usuario', on_delete=models.DO_NOTHING, default='')
    diaHoraInicio = models.DateTimeField()
    diaHoraFim = models.DateTimeField()

class Chamado(models.Model):

    STATUS_CHOICE = ((True,"Sim"),(False,"Não"))

    id_chamado = models.IntegerField(primary_key=True)
    chamado = models.CharField(max_length=200)
    reserva = models.ForeignKey(ReservaSemanal, on_delete=models.DO_NOTHING)
    resolvido = models.BooleanField(choices=STATUS_CHOICE, blank=True, default=False)


    def __str__(self):
        return self.reserva.local.nome + ' ' + self.reserva.matSolicitante.nome

class ReservaRecurso(models.Model):
    idRecurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    docente = models.ForeignKey(Usuario, limit_choices_to={'tipo__tipo': 'Docente'}, on_delete=models.CASCADE)
    dia = models.DateField()
    horaInicio = models.TimeField()
    horaFim = models.TimeField()

    def __str__(self):
        return f'Reserva {self.idRecurso} para {self.docente} em {self.dia} das {self.horaInicio} às {self.horaFim}'