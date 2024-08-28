from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from json import dumps
from populate_horarios import criar_horarios
from rolepermissions.roles import assign_role
from django.contrib.messages import get_messages 
from app.bo.horarios import converter_horarios_back, get_str_horarios


class TestFront(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='usuario_de_teste', password='pass')
        assign_role(self.user, 'servidor')
        self.client.login(username='usuario_de_teste', password='pass')
        
               
    def test_login(self):
        login = self.client.login(username='usuario_de_teste', password='pass')
        self.assertTrue(login)

        res = self.client.get(reverse('cad_local'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_home(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
            
    def test_cad_local_get(self):
        res = self.client.get(reverse('cad_local'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cad_local_post(self):
        res = self.client.post(reverse('cad_local'), data={
            'nome':'B3',
            'bloco':'B',
            'capacidade':'45', 
            'tipo':'Sala'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_sucess_page(self):
        res = self.client.get(reverse('success_page'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_cad_recurso_get(self):
        res = self.client.get(reverse('cadastro-recurso'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_reserva_recurso_get(self):
        res = self.client.get(reverse('reserva_recurso'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_reserva_recurso_post(self):
        res = self.client.post(reverse('reserva_recurso'), 
            data={
                'descricao':'SEMANA DA INFORMÁTICA',
                'horarios': 'M1',
                'dias':'1',
                'qtd_pessoas':10,
                'bloco':'B',
                'local': 'B1',
                'matSolicitante':'202401'
            }
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_tipo_reserva_get(self):
        res = self.client.get(reverse('cad_reserva'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_reserva_semanal_get(self):
        res = self.client.get(reverse('cad_reserva_semanal'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_reserva_semanal_post(self):
        res = self.client.post(reverse('cad_reserva_semanal'), 
            data={
                'descricao':'SEMANA DA INFORMÁTICA',
                'horarios': 'M1',
                'dias':'1',
                'qtd_pessoas':10,
                'bloco':'B',
                'local': 'B1',
                'matSolicitante':'202401'
            })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_cadastro_reserva_dia_get(self):
        res = self.client.get(reverse('cad_reserva_dia'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_reserva_dia_post(self):
        res = self.client.post(reverse('cad_reserva_dia'), 
            data={
                'descricao':'SEMANA DA INFORMÁTICA',
                'horarios': 'M1',
                'dias':'1',
                'qtd_pessoas':10,
                'bloco':'B',
                'local': 'B1',
                'matSolicitante':'202401'
            })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_get_locais_post(self):
        res = self.client.post(reverse('getLocais'), 
            data=dumps({
                'horarios': ['M1'],
                'dias':'1',
                'pessoas':10,
                'bloco':'B',
            }), content_type='application/json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_get_locais_dia_post(self):
        criar_horarios()
        data={
                'diaInicio': '2024-08-13T19:00',
                'diaFim':'2024-08-14T22:00',
                'pessoas':10,
                'bloco':'B',
                'horario':'4N1'
            }
        res = self.client.post(reverse('getLocaisDia'), data=dumps(data), content_type='application/json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_cad_recurso_post(self):
        res = self.client.post(reverse('cadastro-recurso'), data={
            'codigo':52,
            'tipo':'HDMI',
            'status':False,
            'funcionando':True
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_efetuar_chamado_get(self):
        res = self.client.get(reverse('efetuar-chamado'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_efetuar_chamado_post(self):
        res = self.client.post(reverse('efetuar-chamado'), data={'chamado':'HDMI não funciona!','reserva':1})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_cadastro_tipo_recurso_get(self):
        res = self.client.get(reverse('cadastro-tipo-recurso'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_cadastro_tipo_recurso_post(self):
        res = self.client.post(reverse('cadastro-tipo-recurso'), data={'tipo':'HDMI'})
        messages = list(get_messages(res.wsgi_request))
        self.assertTrue(any(msg.message == 'Tipo de recurso cadastrado com sucesso!' for msg in messages))

    def test_get_locais_post(self):
        res = self.client.post(reverse('getLocais'), 
            data=dumps({
                'horarios': ['M1'],
                'dias':'1',
                'pessoas':10,
                'bloco':'B',
            }), content_type='application/json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_listar_reservas_get(self):
        res = self.client.get(reverse('listar-reservas'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_filtros_reserva_get(self):
        res = self.client.get(reverse('filtros-reserva'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_filtrar_reservas_get(self):
        res = self.client.get(reverse('filtrar-reservas'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_reserva_details_get(self):
        res = self.client.get(reverse('reservaDetails'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_tipo_reserva_get(self):
        res = self.client.get(reverse('cad_reserva'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_reserva_semanal_get(self):
        res = self.client.get(reverse('cad_reserva_semanal'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_reserva_semanal_post(self):
        res = self.client.post(reverse('cad_reserva_semanal'), 
            data={
                'descricao':'SEMANA DA INFORMÁTICA',
                'horarios': 'M1',
                'dias':'1',
                'qtd_pessoas':10,
                'bloco':'B',
                'local': 'B1',
                'matSolicitante':'202401'
            })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_cadastro_Reserva_dia_get(self):
        res = self.client.get(reverse('cad_reserva_dia'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_Reserva_dia_post(self):
        res = self.client.post(reverse('cad_reserva_dia'), 
            data={
                'descricao':'SEMANA DA INFORMÁTICA',
                'horarios': 'M1',
                'dias':'1',
                'qtd_pessoas':10,
                'bloco':'B',
                'local': 'B1',
                'matSolicitante':'202401'
            })
        self.assertEqual(res.status_code, status.HTTP_200_OK)

class TestBO(TestCase):
    def test_converter_horarios_back(self):
        horarios = ['2A', '2B', '3A', '3C', '5B']
        resultado = converter_horarios_back(horarios)
        
        self.assertEqual(resultado['dias'], ['2', '3', '5'])
        
        self.assertEqual(resultado['horarios'], ['A', 'B', 'C'])
        
        horarios_repetidos = ['2A', '2A', '3B', '3B', '5C']
        resultado_repetidos = converter_horarios_back(horarios_repetidos)
        
        self.assertEqual(resultado_repetidos['dias'], ['2', '3', '5'])
        
        self.assertEqual(resultado_repetidos['horarios'], ['A', 'B', 'C'])

    def test_get_str_horarios(self):
        horarios = ['2A', '2B', '3A', '3C', '5B']
        resultado = get_str_horarios(horarios)
        
        self.assertEqual(resultado, '235ABC')
        
        horarios_repetidos = ['2A', '2A', '3B', '3B', '5C']
        resultado_repetidos = get_str_horarios(horarios_repetidos)
        
        self.assertEqual(resultado_repetidos, '235ABC')

        horarios_unico = ['2A']
        resultado_unico = get_str_horarios(horarios_unico)
        
        self.assertEqual(resultado_unico, '2A')
        
        horarios_consecutivos = ['2A', '3A', '4A']
        resultado_consecutivos = get_str_horarios(horarios_consecutivos)
        
        self.assertEqual(resultado_consecutivos, '234A')

        horarios_dias_iguais = ['2A', '2B', '2C']
        resultado_dias_iguais = get_str_horarios(horarios_dias_iguais)
        
        self.assertEqual(resultado_dias_iguais, '2ABC')