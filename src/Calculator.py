def addition(x, y):
    a = x + y
    return a


def subtraction(x, y):
    a = x - y
    return a


def multiplication(x, y):
    a = x*y
    return a


def division(x, y):
    a = x/y
    return a


def square(x):
    a = x*x
    return a


class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result = x
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
