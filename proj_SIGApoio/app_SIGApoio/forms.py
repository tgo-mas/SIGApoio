from django import forms
from .models import Recurso, TipoRecurso, Local

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
        
class LocalForm(forms.ModelForm):
    class Meta:
        model= Local
        fields= "__all__"