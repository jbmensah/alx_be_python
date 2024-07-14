import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

	def setUp(self):
		"""Set up the SimpleCalculator instance before each test."""
		self.calc = SimpleCalculator()

	def tearDown(self):
		pass

	def test_addition(self):
		"""Test the addition method."""
	    self.assertEqual(self.calc.add(2, 3), 5)
	    self.assertEqual(self.calc.add(-1, 1), 0)
	    self.assertEqual(self.calc.add(10, 5), 15)
	    self.assertEqual(self.calc.add(-1, -1), -2)

	def test_subtract(self):
		"""Test the subtraction method."""
	    self.assertEqual(self.calc.subtract(2, 3), -1)
	    self.assertEqual(self.calc.subtract(10, 5), 5)
	    self.assertEqual(self.calc.subtract(-1, -1), 0)

	def test_multiply(self):
		"""Test the multiplication method."""
	    self.assertEqual(self.calc.multiply(2, -3), -6)
	    self.assertEqual(self.calc.multiply(10, 5), 50)
	    self.assertEqual(self.calc.multiply(-1, -1), 1)

	def test_divide(self):
	    """Test the division method."""
	    self.assertEqual(self.calc.divide(10, 5), 2)
	    self.assertEqual(self.calc.divide(-1, -1), 1)
	    self.assertEqual(self.calc.divide(-1, 1), -1)
	    # self.assertEqual(self.calc.divide(10, 0), None)

		with self.assertRaises(ZeroDivisionError):
			self.calc.divide(10, 0)

if __name__ == '__main__':
	unittest.main()