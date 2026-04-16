# this is also the least square method, i guess.

import numpy as np
import matplotlib.pyplot as plt

# x = np.array([1,2,3,4,5,6,7,8,9,10])
# y = np.array([11,12,13,14,15,16,17,18,19,20])

x = np.random.randint(1, 20, size=10)
y = np.random.randint(20, 40, size=10)

# calculating the matrix A,B
# just by using the sum function it'a so done

a_11 = np.sum(x**2)
a_12 = np.sum(x)
a_21 = np.sum(x)
a_22 = len(x)
b_11 = np.sum(x*y)
b_21 = np.sum(y)

A = np.array([[a_11,a_12],
              [a_21,a_22]])

inv_A = np.linalg.inv(A)

B = np.array([[b_11],
              [b_21]])

X = inv_A @ B #for the matrix multiplication it's @
print(X)


# additional part
m = X[0,0]
c = X[1,0]

y_fit = m*x + c

plt.scatter(x,y)
plt.plot(x,y_fit)
plt.show()