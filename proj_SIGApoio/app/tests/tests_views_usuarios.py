from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from json import dumps
from populate_horarios import criar_horarios
from django.contrib.messages import get_messages 
from django.http import HttpResponse
from app.views import login

class TestUsuario(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='usuario_de_teste', password='pass')
        self.client.login(username='usuario_de_teste', password='pass')

        self.data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'confirm_email': 'testuser@example.com',
            'password': 'pass',
            'confirm_password': 'testpassword',
            'tipo_usuario': 'servidor'  # ou 'bolsista'
        }


    def test_cadastrao_usuario_get(self):
        #primeiro testar sem permissão
        res = self.client.get(reverse('cadastro_usuario'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, "Seu usuário não tem permissão de acessar essa página")

        assign_role(self.user, 'servidor')
        #agora novamente com permissão
        res = self.client.get(reverse('cadastro_usuario'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'registration/registration_form.html')

    def test_cadastro_usuario_post(self):
        assign_role(self.user, 'servidor')
        res = self.client.post(reverse('cadastro_usuario'), data=self.data)
        self.assertContains(res, "As senhas não coincidem")

        self.data['confirm_password'] = 'pass'
        res = self.client.post(reverse('cadastro_usuario'), data=self.data)
        self.assertEqual(res.status_code, status.HTTP_302_FOUND)
        self.assertTrue(User.objects.filter(username='testuser').exists())

        res = self.client.post(reverse('cadastro_usuario'), data=self.data)
        self.assertContains(res, "Já existe usuario cadastrado")

        self.data['username'] = 'usuario_2'
        res = self.client.post(reverse('cadastro_usuario'), data=self.data)
        self.assertContains(res, "Já existe login com esse e-mail")

    def test_login_usuario_get(self):
        res = self.client.get(reverse('login'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

#    'cadastro_usuario'),
#    'logout'),
#    'remover_local'),
#    'cad_local'),
