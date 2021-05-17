from math import *

def g(x):
    return sin(x) * cos(x) + exp(2*x) + 2*x**4 - 10

def derive(function, value):
    h = 0.00000000001
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom    # Returns the slope to the third decimal
    return float("%.3f" % slope)

print(derive(g, -1))
