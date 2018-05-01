from django.test import TestCase
from api.models import preexisting_models

# Django, Writing and Running Unit Tests: https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Django, Automated Unit Testing Tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial05/

class ExampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        self.assertTrue(True)
class ExampleModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_model(self):
        self.assertTrue(True)