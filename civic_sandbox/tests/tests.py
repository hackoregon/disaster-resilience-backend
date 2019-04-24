from django.test import TestCase, SimpleTestCase, TransactionTestCase
from api.models import preexisting_models
from rest_framework.test import APIClient
from rest_framework import status
import json
from civic_sandbox import packages

# Django, Writing and Running Unit Tests: https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Django, Automated Unit Testing Tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial05/


class SandboxAPIEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.datasets = ['foundations/censusresponse','foundations/landslide/','foundations/liquefaction','foundations/shaking','slides/poi/']
    def test_list_responses(self):
        for endpoint in self.datasets:
            response = self.client.get('/disaster-resilience/sandbox/'+endpoint+'/')
            assert response.status_code == status.HTTP_200_OK
    def test_detail_responses(self):
        for endpoint in self.datasets:
            response = self.client.get('/disaster-resilience/sandbox/'+endpoint+"/1/")
            assert response.status_code == status.HTTP_200_OK

class PackageInfoEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_package_info_response(self):
        response = self.client.get('/disaster-resilience/sandbox/package_info/')
        assert response.status_code == status.HTTP_200_OK   

    def test_package_info_value(self):
        response = self.client.get('/disaster-resilience/sandbox/package_info/')
        assert response.status_code == status.HTTP_200_OK  
        data = json.loads(response.content)
        assert packages.package_info == data
