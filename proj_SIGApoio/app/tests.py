from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.
class TestFront(TestCase):
    def setUp(self):
        self.client = APIClient()
               
    def test_home(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
            
    def test_cad_local_get(self):
        res = self.client.get(reverse('cad_local'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cad_local_post(self):
        res = self.client.post(reverse('cad_local'), data={})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_sucess_page(self):
        res = self.client.get(reverse('success_page'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_cad_recurso_get(self):
        res = self.client.get(reverse('cadastro-recurso'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cad_recurso_post(self):
        res = self.client.post(reverse('cadastro-recurso'), data={})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_efetuar_chamado_get(self):
        res = self.client.get(reverse('efetuar-chamado'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_efetuar_chamado_post(self):
        res = self.client.post(reverse('efetuar-chamado'), data={})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_cadastro_tipo_recurso_get(self):
        res = self.client.get(reverse('cadastro-tipo-recurso'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_cadastro_tipo_recurso_post(self):
        res = self.client.post(reverse('cadastro-tipo-recurso'), data={})
        self.assertEqual(res.status_code, status.HTTP_200_OK)