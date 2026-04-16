# not written by me
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return 3*np.exp(-x) - 0.4*y

n = 100
h = 0.001

x = np.zeros(n)
y = np.zeros(n)

# Initial condition
y[0] = 0  

for i in range(n-1):
    k1 = f(x[i], y[i])
    k2 = f(x[i] + h, y[i] + k1)
    
    y[i+1] = y[i] + (h/2)*(k1 + k2)
    x[i+1] = x[i] + h # here the x is needed to calculate the plot

plt.plot(x, y)
plt.show()
