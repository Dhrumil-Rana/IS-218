import unittest
from Calculator import Calculator
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(self.calculator, Calculator)

if __name__ == '__main__':
    unittest.main()