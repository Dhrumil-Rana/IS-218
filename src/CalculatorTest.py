import unittest
from Calculator import Calculator
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_property_calculator(self):
        self.assertEqual(self.calculator.result, 4)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(8, 4), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_multiple_method_calculator(self):
        self.assertEqual(self.calculator.multiply(4, 4), 16)
        self.assertEqual(self.calculator.result, 16)

    def test_division_method_calculator(self):
        self.assertEqual(self.calculator.div(4, 4), 1)
        self.assertEqual(self.calculator.result, 1)


if __name__ == '__main__':
    unittest.main()
