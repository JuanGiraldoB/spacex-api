from django.test import TestCase
from .views import add_two_numbers


class TestExample(TestCase):

    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(2,2), 4)