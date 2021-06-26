import unittest
from Calculator import Calculator
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_result_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 4)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(8, 4), 4)
        self.assertEqual(calculator.result, 4)


if __name__ == '__main__':
    unittest.main()
