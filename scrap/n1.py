# hardcore method to simulate sine

import math as m
import numpy as np
import matplotlib.pyplot as plt

dft_sin = np.zeros(360)
t_x = np.linspace(0,2*np.pi,360)

i = 0
for s in range(0, 360, 1):
    rad = m.radians(s)
    dft_sin[i] = m.sin(rad)
    i = i + 1


print(dft_sin)
plt.plot(t_x, dft_sin)
plt.show()
