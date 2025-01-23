"""
Sample Tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc Module."""
    
    def test_add_numbers(self):
        """test number add together"""
        res = calc.add(4, 5)
        self.assertEqual(res,9)
    
