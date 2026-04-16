import matplotlib.pyplot as plt
import numpy as np

r = 100
v_s = 10
c = 100e-6
max_t = 10
tow = r*c

v_c = np.zeros(max_t)
time = np.zeros(max_t)
delta_t = 0.1e-3
v_c[0] = 0

for n in range(0,max_t - 1):
    v_c[n+1] = v_c[n] + ((v_s - v_c[n])*delta_t) / tow
    time[n+1] = n*delta_t

plt.stem(time, v_c)
plt.show()
