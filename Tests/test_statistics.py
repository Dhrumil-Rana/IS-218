import unittest
import statistics
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 4.25)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, statistics.mode(self.testData))

    def test_median_calculator(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, statistics.median(self.testData))

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.testData)
        self.assertEqual(variance, statistics.variance(self.testData))

    def test_std_calculator(self):
        std = self.statistics.standard_deviation(self.testData)
        self.assertEqual(round(std, 5), round(statistics.stdev(self.testData), 5))


if __name__ == '__main__':
    unittest.main()
