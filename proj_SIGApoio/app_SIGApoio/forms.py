from django import forms
from .models import Local, Emprestimo, Reserva

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'bloco', 'local', 'numero']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['idRecurso', 'matUsuario']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['horarios', 'local', 'matResponsavel', 'matSolicitante']
