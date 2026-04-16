# the best code so far
# noice!

import numpy as np
import matplotlib.pyplot as plt

def lagrange(x_points, y_points, x):
    n = len(x_points)
    P = 0
    for k in range(n):
        L_k = 1 # l_k is in multiplication so that's why is's 1
        for j in range(n):
            if j != k:
                L_k *= (x - x_points[j]) / (x_points[k] - x_points[j])
        P += y_points[k] * L_k
    return P

# Data points
x_pts = np.array([1, 3, 5])
y_pts = np.array([2, 4, 0])

# Interpolate
x_range = np.linspace(0, 6, 200)
y_range = [lagrange(x_pts, y_pts, xi) for xi in x_range]

# for xi in x_range:


plt.plot(x_range, y_range, label="Interpolated")
plt.scatter(x_pts, y_pts, color='red', zorder=5, label="Known points")
plt.legend()
plt.show()