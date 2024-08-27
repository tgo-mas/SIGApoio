from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from json import dumps
from populate_horarios import criar_horarios
from django.contrib.messages import get_messages 
from app.models import Usuario, TipoUsuario, TipoLocal, Local
from app.forms import LocalForm


class TestEmprestimo(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='usuario_de_teste', password='pass')
        assign_role(self.user, 'servidor')
        self.client.login(username='usuario_de_teste', password='pass')

        self.tipo_usuario1 = TipoUsuario.objects.create(tipo='bolsista')
        self.tipo_usuario2 = TipoUsuario.objects.create(tipo='usuario')

        self.usuario1 = Usuario.objects.create(matricula=123, nome="userTeste1", email="user1@teste.com", tipo=self.tipo_usuario1)
        self.usuario2 = Usuario.objects.create(matricula=234, nome="userTeste2", email="user2@teste.com", tipo=self.tipo_usuario2)

        self.tipo_local = TipoLocal.objects.create(tipo='Sala')

    def test_cadastrar_local_get(self):
        res = self.client.get(reverse('cad_local'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsInstance(res.context['form'], LocalForm)

    def test_cadastrar_local_post(self):
        data = {
            'nome': 'Local Teste',
            'bloco': 'A',
            'capacidade': 50,
            'tipo': self.tipo_local
        }

        response = self.client.post(reverse('cad_local'), data)

        self.assertNotEqual(Local.objects.count(), 0)
        self.assertEqual(Local.objects.first().nome, 'Local Teste')

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(msg.message == 'Local foi cadastrado com sucesso!' for msg in messages))
        
    def test_listar_locais_get(self):
        res = self.client.get(reverse('listar_local'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_editar_local_get_404(self):
        res = self.client.get(reverse('editar_local', kwargs={'pk': 1}))
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    #def test_editar_local_get(self):
    #    res = self.client.get(reverse('editar_local', kwargs={'pk': self.local1.pk}))
    #    self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_editar_local_post(self):
        self.local1 = Local.objects.create(
            nome='Local 1',
            bloco='A',
            capacidade=50,
            tipo=self.tipo_local
        )
        response = self.client.post(reverse('editar_local', kwargs={'pk': self.local1.pk}), {
            'nome': 'Local 2', 
            'bloco': 'A',
            'capacidade': 50,
            'tipo': self.tipo_local
        })
        self.assertRedirects(response, reverse('listar_local'))
        self.local1.refresh_from_db()
        self.assertEqual(self.local1.nome, 'Local 2')


#    'listar_local'),
#    'editar_local'),
#    'remover_local'),
#    'cad_local'),
