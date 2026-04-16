# some changes needed

import numpy as np
import matplotlib.pyplot as plt

time=np.linspace(0,60e-3,600)
Ts=20e-3/200

f=50
signal= 10*np.sin(2*np.pi*f*time)
N=len(signal) # 600

I_result=np.zeros(N)
area=0

for i in range(N-1):
    I_result[i+1]= area + 0.5*Ts*(signal[i+1]+signal[i])
    area=I_result[i+1]


plt.plot(time,signal)
plt.plot(time,I_result*(2*np.pi*50))
plt.show()