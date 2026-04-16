# i don't know why i wrote this code

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(1, 20, size=10)
y = np.random.randint(20, 40, size=10)

# model
def predict(x,a,b):
    return a*x + b

# error f'n
def error(a, b):
    y_pred = predict(x,a,b)
    return np.sum((y - y_pred)**2)

# brute-force search
best_a = 0
best_b = 0

min_error = float('inf')

# trying different values
for a in range(-10, 10, 100):
    for b in range(-10, 10, 100):
        e = error(a, b)
        best_a = a
        best_b = b

# o/p
print("best fit line")
print(f"y = {best_a}x + {best_b}")
print(f"error = {min_error}")