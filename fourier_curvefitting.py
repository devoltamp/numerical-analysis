# make up the mathematical formula to cover up the code 
# still pending


import numpy as np
import matplotlib.pyplot as plt


# Generating data
base_freq=50
t_x=np.linspace(0,40e-3,41)
complete_signal=20*np.sin(2*np.pi*50*t_x)+20*np.sin(2*np.pi*150*t_x)
# print(t_x)
# print(complete_signal)
signal=complete_signal[0:20]
t=t_x[0:20]
plt.plot(t,signal)
plt.show()


# Fourier
N=len(signal)
dft_mag=np.zeros(N)
dft_phase=np.zeros(N)
for k in range(0,N):

    temp1=0
    temp2=0
    for n in range(0,N):
        temp1=temp1+ (signal[n]*np.cos(2*np.pi*k*n/N))
        temp2=temp2+ (signal[n]*np.sin(2*np.pi*k*n/N))
    dft_mag[k]=np.sqrt(temp1**2 + temp2**2)*(2/N)
    dft_phase[k]=np.arctan2(temp2,temp1)

    # temp1 = real 
    # temp2 = img


k=np.linspace(0,N-1,20)
plt.bar(k,dft_mag)
plt.xticks(k,k)
plt.show()
        

# Fourier Series
dft_mag=dft_mag*0.5
re_sig=np.zeros(N)
for n in range(0,N):
    re_sig[n]=0
    for k in range(0,N):
        re_sig[n]= re_sig[n]+( dft_mag[k]*np.cos(2*np.pi*k*base_freq*t[n]  + dft_phase[k])  )
        # base_freq = 50 = f_0
        
plt.plot(t,-1*re_sig)
plt.plot(t,signal-(-1*re_sig)) 
# it will plot a zero line at 0 because the difference will be zero that's noice
plt.show()