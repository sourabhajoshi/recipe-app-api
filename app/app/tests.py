"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc

class calcTests(SimpleTestCase):
  
  def test_add_numbers(self):
    """Test adding numbers"""
    res = calc.add(5, 6)
    self.assertEqual(res, 11)
    
  def test_sub_numbers(self):
    res = calc.sub(11, 10)
    self.assertEquals(res, 1)
    
  def test_mul_numbers(self):
    res = calc.mul(2, 3)
    self.assertEquals(res, 6)