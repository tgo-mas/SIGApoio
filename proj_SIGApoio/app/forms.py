from django import forms
from .models import Recurso, TipoRecurso, Local, TipoLocal, Chamado, Reserva


class TipoRecursoForm(forms.Form, forms.ModelForm):
    tipo = forms.CharField(
        label = 'Tipo',
        widget = forms.TextInput(attrs={'class':'form-control'}) 
    )
    
    class Meta:
        model = TipoRecurso
        fields = ['tipo']

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

class LocalForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(
        queryset=TipoLocal.objects.all(),
        label='Tipo de Local',
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'color: black'})
    )

    class Meta:
        model = Local
        fields = "__all__"