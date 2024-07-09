from django import forms
from .models import Recurso, TipoRecurso, Local, Usuario, Reserva

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
        
class ReservaForm(forms.ModelForm, forms.Form):
    horarios = forms.ChoiceField(
        label="Horários",
        choices=[
            ('M1', 'M1'), ('M2', 'M2'), ('M3', 'M3'), ('M4', 'M4'), ('M5', 'M5'), ('M6', 'M6'),
            ('T1', 'T1'), ('T2', 'T2'), ('T3', 'T3'), ('T4', 'T4'), ('T5', 'T5'), ('T6', 'T6'),
            ('N1', 'N1'), ('N2', 'N2'), ('N3', 'N3'), ('N4', 'N4')
        ],
        widget=forms.Select(attrs={'onChange': 'fetchLocais()'})
    )
    
    dias = forms.ChoiceField(
        label='Dia(s)',
        choices=[
            ('2', 'Segunda'),
            ('3', 'Terça'),
            ('4', 'Quarta'),
            ('5', 'Quinta'),
            ('6', 'Sexta'),
        ],
        widget=forms.Select(attrs={'onChange': 'fetchLocais()'})
    )
    
    matResponsavel = forms.ChoiceField(
        label="Responsável",
        choices=Usuario.objects.values_list('matricula', 'nome')
    )
    
    matSolicitante = forms.ChoiceField(
        label="Solicitante",
        choices=Usuario.objects.values_list('matricula', 'nome')
    )    
    
    locais = forms.ChoiceField(
        label="Locais",
        widget=forms.Select(
            attrs={'id': 'locais', 'class': 'form-select'}
        )   
    )

    class Meta:
        model = Reserva
        fields = ['horarios', 'dias', 'matResponsavel', 'matSolicitante', 'locais']
    