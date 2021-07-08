from Calculator.Addition import addition
from Calculator.Division import division


def median(data):
    data.sort()
    length = len(data)
    med = 0

    if length % 2 == 0:
        v1 = length/2
        v2 = (length/2) + 1

        v1 = int(v1) - 1
        v2 = int(v2) - 1
        addmed = addition(data[v1], data[v2])
        med = division(2, addmed)
    else:
        v1 = (length + 1) / 2
        v1 = int(v1) - 1
        med = data[v1]

    return med



