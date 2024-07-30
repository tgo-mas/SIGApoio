from django import forms
from django.db import connection
from .models import Recurso, TipoRecurso, Local, TipoLocal, Usuario, ReservaSemanal, ReservaDiaUnico, ReservaMensal, Chamado


BLOCOS_CHOICES = [('A', 'Bloco A'), ('B', 'Bloco B'), ('C', 'Bloco C'), ('D', 'Bloco D'), ('Aud', 'Auditórios'), ('Lab', 'Laboratórios')]

def get_usuario_choices():
    try:
        if 'app_usuario' in connection.introspection.table_names():
            print('achou usuário')
            return [(usuario.matricula, usuario.nome) for usuario in Usuario.objects.all()]
        else:
            return []
            print('nao achou usuário')
        
    except Exception as e:
        print('deu erro')
        return []


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
        queryset=ReservaSemanal.objects.all(),
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
        model= Local
        fields= "__all__"
        
class ReservaForm(forms.ModelForm, forms.Form):
    descricao = forms.CharField(
        label='Descrição',
        widget=forms.TextInput(
            attrs={'class': 'form-control blue-text gray-back me-4'}
        )
    )
    
    horarios = forms.MultipleChoiceField(
        label="Horários",
        choices=[
            ('M1', 'M1'), ('M2', 'M2'), ('M3', 'M3'), ('M4', 'M4'), ('M5', 'M5'), ('M6', 'M6'),
            ('T1', 'T1'), ('T2', 'T2'), ('T3', 'T3'), ('T4', 'T4'), ('T5', 'T5'), ('T6', 'T6'),
            ('N1', 'N1'), ('N2', 'N2'), ('N3', 'N3'), ('N4', 'N4')
        ],
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select gray-back blue-text me-4'
            }
        )
    )
    
    dias = forms.MultipleChoiceField(
        label='Dia(s)',
        choices=[
            ('2', 'Segunda'),
            ('3', 'Terça'),
            ('4', 'Quarta'),
            ('5', 'Quinta'),
            ('6', 'Sexta'),
        ],
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select gray-back blue-text me-4'
            }
        )
    )
    
    qtd_pessoas = forms.IntegerField(
        max_value=250,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control gray-back blue-text me-4'
            },
        )
    )
    
    bloco = forms.ChoiceField(
        choices=BLOCOS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select gray-back blue-text me-4'
            }
        )
    )
    
    matSolicitante = forms.ChoiceField(
        label="Solicitante",
        choices=get_usuario_choices(),
        widget=forms.Select(
            attrs={
                'class': 'form-select gray-back blue-text me-4'
            }
        )
    )    
    
    local = forms.ChoiceField(
        label="Local",
        widget=forms.Select(
            attrs={
                'class': 'form-select gray-back blue-text me-4'
            }
        )
    )

    class Meta:
        model = ReservaSemanal
        fields = ['horarios', 'dias', 'qtd_pessoas', 'matSolicitante', 'local']
        
    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['local'].queryset = Local.objects.none()

        if 'horarios' and 'dias' in self.data:
            try:
                self.fields['local'].queryset = \
                    Local.objects.all().order_by('nome')
                print(self.fields['local'].queryset)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Horarios queryset
        elif self.instance.pk:
            self.fields['local'].queryset = Local.objects.none()

class ReservaDiaForm(forms.ModelForm, forms.Form):
    descricao = forms.CharField(
        label='Descrição',
        widget=forms.TextInput(
            attrs={'class': 'form-control blue-text gray-back me-4'}
        )
    )
    
    local = forms.ChoiceField(
        label='Local',
        widget=forms.Select(
            attrs={'class': 'form-select blue-text gray-back me-4'}
        )
    )
    
    diaHoraInicio = forms.DateTimeField(
        label="Início da reserva",
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control blue-text gray-back me-4', 'type': 'datetime-local'}
        )
    )
    
    diaHoraFim = forms.DateTimeField(
        label="Fim da reserva",
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control blue-text gray-back me-4', 'type': 'datetime-local'}
        )
    )
    
    qtd_pessoas = forms.IntegerField(
        max_value=250,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control gray-back blue-text me-4'
            },
        )
    )
    
    bloco = forms.ChoiceField(
        choices=BLOCOS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select gray-back blue-text me-4'
            }
        )
    )
    
    matSolicitante = forms.ChoiceField(
        label='Solicitante',
        choices=get_usuario_choices(),
        widget=forms.Select(
            attrs={'class': 'form-select blue-text gray-back me-4'}
        )
    )
    
    class Meta:
        model = ReservaDiaUnico
        fields = ['descricao', 'diaHoraInicio', 'diaHoraFim', 'local', 'matSolicitante']

class ReservaMensalForm(forms.ModelForm, forms.Form):
    descricao = forms.CharField(
        label='Descrição',
        widget=forms.TextInput(
            attrs={'class': 'form-control blue-text gray-back me-4'}
        )
    )
    
    local = forms.ChoiceField(
        label='Local',
        widget=forms.Select(
            attrs={'class': 'form-select blue-text gray-back me-4'}
        )
    )
    
    dias = forms.ChoiceField(
        label="Dias",
        widget=forms.DateInput(
            attrs={'class': 'form-control blue-text gray-back me-4', 'type': 'date'}
        )
    )
    
    repeticoes = forms.IntegerField(
        label="Repetições (meses)",
        widget=forms.NumberInput(
            attrs={'class': 'form-control blue-text gray-back me-4'}
        )
    )
    
    qtd_pessoas = forms.IntegerField(
        max_value=250,
        initial=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control gray-back blue-text me-4'
            },
        )
    )
    
    bloco = forms.ChoiceField(
        choices=BLOCOS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select gray-back blue-text me-4'
            }
        )
    )
    
    matSolicitante = forms.ChoiceField(
        label='Solicitante',
        choices=get_usuario_choices(),
        widget=forms.Select(
            attrs={'class': 'form-select blue-text gray-back me-4'}
        )
    )
    
    class Meta:
        model = ReservaMensal
        fields = ['descricao', 'dias', 'repeticoes', 'local', 'matSolicitante']
   