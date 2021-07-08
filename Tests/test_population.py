import unittest
from RandomGenerator.Random import Random
from PopulationSampling.populationSampling import PopulationSampling


class PopulationSamplingTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.Random = Random()
        self.populationSampling = PopulationSampling()

    def test_instantiate_random_generator(self):
        self.assertIsInstance(self.Random, Random)

    def test_instantiate_population_sampling(self):
        self.assertIsInstance(self.populationSampling, PopulationSampling)

    def test_simple_random_sampling(self):
        testing = self.Random.random_list(0, 15, 50, 2)
        result = self.populationSampling.simple_random_sampling(testing, 10, 5)
        return result
        #self.assertEqual(self.populationSampling.simple_random_sampling(testing, 10, 5), result)
        testing.clear()

    def test_confidence_interval(self):
        testing = [5, 6, 3, 5, 1, 3, 7, 3]
        self.assertEqual(self.populationSampling.confidence_interval(testing), [5.482802, 2.767198])
        testing.clear()

    def test_margin_error(self):
        testing = [5, 6, 3, 5, 1, 3, 7, 3]
        self.assertEqual(round(self.populationSampling.margin_error(testing), 6), 8.51011)
        testing.clear()


if __name__ == '__main__':
    unittest.main()