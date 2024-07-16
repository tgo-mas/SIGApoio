from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

RECURSO_URL = reverse('app:cadastro-recurso')


# Create your tests here.
class TestFront(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_cad_recurso(self):
        res = self.client.get(RECURSO_URL)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
