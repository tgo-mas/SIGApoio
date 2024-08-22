from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from json import dumps
from populate_horarios import criar_horarios
from app.models import TipoRecurso, Recurso
from app.forms import TipoRecursoForm, RecursoForm


class TestFront(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='usuario_de_teste', password='pass')
        self.client.login(username='usuario_de_teste', password='pass')
        self.tipo_recurso = TipoRecurso.objects.create(tipo='HDMI')
        self.form_data = {
            'codigo': 1234,
            'tipo': self.tipo_recurso.id,
            'funcionando': True, 
            'status':True 
        }
        
    def test_tipo_recurso_form_initialization(self):
        form = TipoRecursoForm()
        self.assertIn('tipo', form.fields)
        self.assertEqual(form.fields['tipo'].label, 'Tipo')
        self.assertEqual(form.fields['tipo'].widget.attrs['class'], 'form-control')

    def test_tipo_recurso_form_valid_data(self):
        form_data = {'tipo': 'HDMI'}
        form = TipoRecursoForm(data=form_data)
        self.assertTrue(form.is_valid())
        tipo_recurso = form.save()
        self.assertEqual(tipo_recurso.tipo, 'HDMI')

    def test_tipo_recurso_form_invalid_data(self):
        form_data = {'tipo': ''}
        form = TipoRecursoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('tipo', form.errors)
        
    def test_recurso_form_initialization(self):
        form = RecursoForm()
        self.assertIn('codigo', form.fields)
        self.assertIn('tipo', form.fields)
        self.assertIn('funcionando', form.fields)
        self.assertEqual(form.fields['codigo'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['tipo'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['funcionando'].widget.attrs['class'], 'form-control')

    def test_recurso_form_valid_data(self):
        form = RecursoForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        recurso = form.save()
        self.assertEqual(recurso.codigo, 1234)
        self.assertEqual(recurso.tipo, self.tipo_recurso)
        self.assertEqual(recurso.funcionando, True)

    def test_recurso_form_invalid_data(self):
        invalid_data = self.form_data.copy()
        invalid_data['codigo'] = ''
        form = RecursoForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('codigo', form.errors)

    def test_recurso_disable_fields_except_funcionando(self):
        form = RecursoForm(data=self.form_data)
        form.disable_fields_except_funcionando()

        self.assertTrue(form.fields['tipo'].disabled)
        self.assertFalse(form.fields['funcionando'].disabled)
        
        self.assertFalse(form.fields['codigo'].required)
        self.assertFalse(form.fields['tipo'].required)