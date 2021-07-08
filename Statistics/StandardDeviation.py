from Statistics.Variance import variance
from Calculator.square_root import square_root

def std(data):
    return square_root(variance(data))
