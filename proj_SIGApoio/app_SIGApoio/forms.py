from django import forms
from .models import Recurso, TipoRecurso, Chamado, Reserva

class RecursoForm(forms.Form, forms.ModelForm):
    codigo = forms.CharField(
        label='Código',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    
    tipo = forms.ModelChoiceField(
        queryset=TipoRecurso.objects.all(),
        label='Tipo',
        widget=forms.Select(attrs={'class':'form-control', 'style':'color: black'})
    )
    
    status = forms.ChoiceField(
        choices=Recurso.STATUS_CHOICE,
        widget=forms.Select(attrs={'class':'form-control', 'style':'color: black'})
    )
    
    funcionando = forms.ChoiceField(
        choices=Recurso.FUNCIONANDO_CHOICE,
        widget=forms.Select(attrs={'class':'form-control', 'style':'color: black'})
    )
    
    class Meta:
        model = Recurso
        fields = ['codigo','tipo', 'status', 'funcionando']  

class ChamadoForm(forms.Form, forms.ModelForm):
    chamado = forms.CharField(
        label='Chamado',
        widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escreva sua mensagem aqui!'})
    )

    reserva = forms.ModelChoiceField(
        queryset=Reserva.objects.all(),
        label='Reserva',
        widget=forms.Select(attrs={'class':'form-control', 'style':'color: black'})
    )

    class Meta:
        model = Chamado
        fields = ['chamado', 'reserva']
