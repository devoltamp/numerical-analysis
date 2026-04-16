# it's fucked up dude

import math as m
import numpy as np
import matplotlib.pyplot as plt

lp = np.zeros(360)
for l in range(360):
    j = 0 
    j = j + 1
    lp[j] = l

sin1 = np.zeros(360)
# x = [1,2,3,4,5,6,7,8,9,10]
# N = len(x)

i = 0
for s in range(0, 360, 1):
    rad = m.radians(s)
    sin1[i] = m.sin(rad)
    i = i + 1

N = len(sin1)
print(N)
dft_mag = np.zeros(N)


for k in range(N):
    temp1 = 0
    temp2 = 0
    for n in range(N):
        angle = 2 * m.pi * k * n / N
        temp1 += sin1[n] * m.cos(angle)
        temp2 -= sin1[n] * m.sin(angle)

    dft_mag[k] = m.sqrt(temp1**2 + temp2**2)

k_vals = np.arange(N)

plt.stem(sin1, dft_mag)
plt.xlabel("k")
plt.ylabel("Magnitude")
plt.title("man idk fourier...")
plt.show()

plt.stem(lp, sin1)
plt.show()