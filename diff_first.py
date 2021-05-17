import numpy as np
import sympy as sym
x = sym.Symbol('x')
def derivative(f,a,method='central',h=0.01):

    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'forward':
        return (f(a + h) - f(a))/h
    elif method == 'backward':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")
        
print(derivative(np.sin ,47))
