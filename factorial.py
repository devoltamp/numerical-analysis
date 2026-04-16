# calculating the value of f'n via a series

import math as m


def my_factorial(a):
    fac = 1
    for a in range(a, 1, -1):
        fac = fac * a
    return fac

def f(x):
    return 0.5 + (x**2)/my_factorial(4) + (x**2)/my_factorial(6)


x = 1 * ((m.e)**(-8))
fx = f(x)
print(f"the function is: {fx}")
