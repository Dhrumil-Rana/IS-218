import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader("Tests/Data/Unit Test Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_addition(self):
        test_data = CsvReader("Tests/Data/Unit Test Addition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_Division(self):
        test_data = CsvReader("Tests/Data/Unit Test Division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.div(round(float(row['Value 1']), 9), round(float(row['Value 2']), 9)),
                             round(result, 9))
            self.assertEqual(round(self.calculator.result, 7), round(result, 7))

    def test_Multiplication(self):
        test_data = CsvReader("Tests/Data/Unit Test Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_Square(self):
        test_data = CsvReader("Tests/Data/Unit Test Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqr(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_Square_root(self):
        test_data = CsvReader("Tests/Data/Unit Test Square Root.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqr_root(row['Value 1']), round(result, 8))
            self.assertEqual(self.calculator.result, round(result, 8))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
