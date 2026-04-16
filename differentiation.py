import numpy as np
import matplotlib.pyplot as plt


time=np.linspace(0,60e-3,600)
Ts=20e-3/200 
f=50
signal= 10*np.sin(2*np.pi*f*time)
N=len(signal)
d_result=np.zeros(N)


for i in range(0,N-1):
    d_result[i+1]=(signal[i+1]-signal[i])/Ts


plt.plot(time,signal)
plt.plot(time,d_result/(2*np.pi*50))
plt.show()