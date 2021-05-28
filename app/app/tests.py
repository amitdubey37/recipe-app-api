from django.test import TestCase
from .calc import add, subtract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """ test two numbers are addding together """
        self.assertEquals(add(2, 5), 7)

    def test_subtract(self):
        """ test if two numbers are subtracted"""
        self.assertEquals(subtract(5, 2), 3)
