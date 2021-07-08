from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Calculator.square import square
from Calculator.Addition import addition
from Calculator.Division import division
import statistics

def variance(data):
    '''
    avgdata = mean(data)
    length = len(data)
    list = []
    total = 0
    for i in data:
        temp = subtraction(avgdata, i)
        list.append(int(square(temp)))
    for j in list:
        total += addition(total, j)
    return division(length-1, total)
'''
    return statistics.variance(data)