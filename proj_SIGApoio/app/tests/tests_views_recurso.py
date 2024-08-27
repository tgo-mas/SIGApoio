from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from json import dumps
from populate_horarios import criar_horarios
from django.contrib.messages import get_messages 
from app.models import Recurso, TipoRecurso, Emprestimo, Usuario, TipoUsuario
from rolepermissions.roles import assign_role

class TestRecurso(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='usuario_de_teste', password='pass')
        self.client.login(username='usuario_de_teste', password='pass')
        assign_role(self.user,'servidor')
        self.tipo_recurso = TipoRecurso.objects.create(tipo='Tipo Teste')  # Ajuste conforme necessário
        
        self.recurso = Recurso.objects.create(
            id_codigo=1,
            codigo=123,
            tipo=self.tipo_recurso,
            status=True,
            funcionando=True
        )

    def test_listar_recurso_get(self):
        res = self.client.get(reverse('listar-recurso'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_recurso_edit_get(self):
        url = reverse('rec_edit', kwargs={'id': self.recurso.pk})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_recurso_edit_post(self):
        url = reverse('rec_edit', kwargs={'id': self.recurso.pk})
        response = self.client.post(url)
        self.assertNotEqual(Recurso.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_recurso_delete_get(self):
        url = reverse('rec_delete', kwargs={'id': self.recurso.pk})
        response = self.client.post(url)
        self.assertEqual(Recurso.objects.count(), 0)
        self.assertRedirects(response, reverse('listar-recurso'))
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(msg.message == 'Recurso excluído com sucesso!' for msg in messages))

class TestEmprestimo(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='usuario_de_teste', password='pass')
        self.client.login(username='usuario_de_teste', password='pass')
        assign_role(self.user,'servidor')

        self.tipo_usuario1 = TipoUsuario.objects.create(tipo='bolsista')
        self.tipo_usuario2 = TipoUsuario.objects.create(tipo='usuario')

        self.usuario1 = Usuario.objects.create(matricula=123, nome="userTeste1", email="user1@teste.com", tipo=self.tipo_usuario1)
        self.usuario2 = Usuario.objects.create(matricula=234, nome="userTeste2", email="user2@teste.com", tipo=self.tipo_usuario2)
        
        self.tipo_recurso = TipoRecurso.objects.create(tipo='Tipo Teste')  # Ajuste conforme necessário
        
        self.recurso = Recurso.objects.create(
            id_codigo=1,
            codigo=123,
            tipo=self.tipo_recurso,
            status=True,
            funcionando=True
        )

        self.emprestimo = Emprestimo.objects.create(
            idRecurso=self.recurso,
            matBolsista=self.usuario1,
            matUsuario=self.usuario2,
        )

        
    def test_cadastro_emprestimo_get(self):
        res = self.client.get(reverse('cadastrar_emprestimo'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_cadastro_emprestimo_post(self):
        res = self.client.post(reverse('cadastrar_emprestimo'), 
            data={
                'idRecurso': self.recurso.pk,
            })
        messages = list(get_messages(res.wsgi_request))
        self.assertTrue(any(msg.message == 'Formulário inválido' for msg in messages))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_emprestimo_listar_get(self):
        self.url = reverse('listar_emprestimos')
        
        response = self.client.get(self.url, {'status': 'ativos'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        emprestimos = response.context['emprestimos']
        self.assertIn(self.emprestimo, emprestimos)

        response = self.client.get(self.url, {'status': 'devolvidos'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        emprestimos = response.context['emprestimos']
        self.assertNotIn(self.emprestimo, emprestimos)

        response = self.client.get(self.url, {'usuario': self.usuario1.nome})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        emprestimos = response.context['emprestimos']
        self.assertIn(self.emprestimo, emprestimos)

        response = self.client.get(self.url, {'solicitante': self.usuario2.nome})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        emprestimos = response.context['emprestimos']
        self.assertIn(self.emprestimo, emprestimos)


    def test_emprestimo_edit_get(self):
        url = reverse('editar_emprestimo', kwargs={'emprestimo_id': self.emprestimo.pk})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_emprestimo_edit_post(self):
        url = reverse('editar_emprestimo', kwargs={'emprestimo_id': self.emprestimo.pk})
        res = self.client.post(url)
        self.assertNotEqual(Emprestimo.objects.count(), 0)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_devolucao_emprestimo_post(self):
        url = reverse('registrar_devolucao', kwargs={'emprestimo_id': self.emprestimo.pk})
        res = self.client.post(url)
        self.assertRedirects(res, reverse('listar_emprestimos'))

    def test_emprestimo_delete_get(self):
        url = reverse('excluir_emprestimo', kwargs={'emprestimo_id': self.emprestimo.pk})
        res = self.client.post(url)
        self.assertEqual(Emprestimo.objects.count(), 0)
        self.assertRedirects(res, reverse('listar_emprestimos'))
        messages = list(get_messages(res.wsgi_request))
        self.assertTrue(any(msg.message == 'Empréstimo excluído com sucesso.' for msg in messages))