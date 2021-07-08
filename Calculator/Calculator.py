from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Division import division

from Calculator.square_root import square_root

from Calculator.multiplication import multiplication
from Calculator.square import square


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def div(self, a, b):
        self.result = division(a, b)
        return round(self.result, 9)

    def sqr_root(self, a):
        self.result = square_root(a)
        return round(self.result, 8)

    def sqr(self, a):
        self.result = square(a)
        return self.result



