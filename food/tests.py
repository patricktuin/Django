from django.test import TestCase

# Create your tests here.
from food.models import Dish, Ingredient
from django.test.client import Client

class FoodMethodTest(TestCase):

	def test_pasta(self):
		response = Client()
		response = response.get('/')
		self.assertEqual(response.status_code!='404', True)
