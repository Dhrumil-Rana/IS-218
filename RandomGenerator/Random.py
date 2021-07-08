import random

class Random:

    def __init__(self):
        pass

    def RanNum(self, first, second):
        return random.randrange(first, second)

    def random_seed(self, first, second, s):
        random.seed(s)
        return random.randrange(first, second)

    def random_list(self, x, y, n, s):
        random.seed(s)
        random_numbers = []
        for r in range(n):
            random_numbers.append(random.randrange(x, y))
        return random_numbers
