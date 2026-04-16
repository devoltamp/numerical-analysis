#import pdb
import numpy as np
import matplotlib.pyplot as plt


Ts=0.001
time=np.arange(0,0.1,Ts)
signal = 10*np.sin((2*np.pi*50*time)-(np.pi/6))

def my_window(i):
    my_data=signal[i:i+20]
    return my_data

def calc_rms(sig_cycle):
    my_rms=0
    for n in range(0,len(sig_cycle)):
        my_rms=my_rms+ (sig_cycle[n]*sig_cycle[n])
    my_rms=np.sqrt(my_rms/20)
    return my_rms

n=int(0.02/0.001)
N=len(time)
sig_cycle=np.zeros(20)
rms=np.zeros(len(signal))

#pdb.set_trace()
for i in range(0,N-n):
    sig_cycle=my_window(i)
    rms[i]=calc_rms(sig_cycle)

plt.plot(rms[0:N-n])
plt.show()
plt.plot(signal)
plt.show