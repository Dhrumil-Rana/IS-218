import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pathlib import Path
from pprint import pprint

Folder_toOpen = Path("/src/testdata/")
file_toOpen = Folder_toOpen / "Unit Test Addition.csv"
file_for_sub = Folder_toOpen / "Unit Test Subtraction.csv"
file_for_mul = Folder_toOpen / "Unit Test Multiplication.csv"
file_for_div = Folder_toOpen / "Unit Test Division.csv"
file_for_sqr = Folder_toOpen / "Unit Test Square.csv"
file_for_sqrt = Folder_toOpen / "Unit Test Square Root.csv"


class MyTestCase1(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        self.test_data = CsvReader(file_toOpen)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader(file_toOpen).data
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        # self.assertEqual(self.calculator.add(2, 2), 4)
        # self.assertEqual(self.calculator.result, 4)

    def test_multiple_method_calculator(self):
        CsvReader.clear_data(self.test_data)
        test_data = CsvReader(file_for_mul).data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_calculator(self):
        CsvReader.clear_data(self.test_data)
        test_data = CsvReader(file_for_div).data
        for row in test_data:
            self.assertEqual(self.calculator.div(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_method_calculator(self):
        CsvReader.clear_data(self.test_data)
        test_data = CsvReader(file_for_sqr).data
        for row in test_data:
            self.assertEqual(self.calculator.sqr(float(row['Value 1'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_root_method_calculator(self):
        CsvReader.clear_data(self.test_data)
        test_data = CsvReader(file_for_sqrt).data
        for row in test_data:
            self.assertEqual(self.calculator.sqr_root(float(row['Value 1'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtract_method_calculator(self):
        CsvReader.clear_data(self.test_data)
        test_data = CsvReader(file_for_sub).data
        # pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        # self.assertEqual(self.calculator.subtract(8, 4), 4)
        # self.assertEqual(self.calculator.result, 4)


if __name__ == '__main__':
    unittest.main()
