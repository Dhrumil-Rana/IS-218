import math


def addition(x, y):
    a = int(x) + int(y)
    return a


def subtraction(x, y):
    a = int(y) - int(x)
    return int(a)


def multiplication(x, y):
    a = float(x)*float(y)
    return float(a)


def division(x, y):
    a = float(y)/float(x)
    return round(float(a), 9)


def square(x):
    a = float(x)*float(x)
    return float(a)


def square_root(x):
    a = math.sqrt(x)
    return round(float(a), 8)


class Calculator:
    result = 0

    def __init__(self):
        self.result = 0
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
        return self.result

    def sqr(self, a):
        self.result = square(a)
        return self.result

    def sqr_root(self, a):
        self.result = square_root(a)
        return self.result
