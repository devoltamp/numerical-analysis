# https://home.iitk.ac.in/~pranab/ESO208/Gauss-Siedel-Jacobi.pdf
# noice code

import numpy as np

A = np.array([[4, 1, 2],
              [3, 5, 1],
              [1, 1, 3]], dtype=float)

b = np.array([4, 7, 3], dtype=float)

tol = 1e-6
max_iter = 100

x1 = x2 = x3 = 0.0

for i in range(max_iter):
    old1, old2, old3 = x1, x2, x3

    x1 = (b[0] - A[0][1]*x2 - A[0][2]*x3) / A[0][0]
    x2 = (b[1] - A[1][0]*x1 - A[1][2]*x3) / A[1][1]
    x3 = (b[2] - A[2][0]*x1 - A[2][1]*x2) / A[2][2]

    if max(abs(x1 - old1), abs(x2 - old2), abs(x3 - old3)) < tol:
        print("Solution:", x1, x2, x3)
        break
else:
    print("Maximum iterations reached")