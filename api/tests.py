from django.test import TestCase
from api.models import preexisting_models

class NeighborhoodUnitsTestCase(TestCase):
    def setUp(self):
        preexisting_models.NeighborhoodUnits.objects.create(name="lion", sound="roar")
        preexisting_models.NeighborhoodUnits.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = preexisting_models.NeighborhoodUnits.objects.get(name="lion")
        cat = preexisting_models.NeighborhoodUnits.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
