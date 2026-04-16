# not written by me thanks to cluade

import numpy as np
import matplotlib.pyplot as plt

# Signal
t = np.linspace(0, 40e-3, 20)
signal = 20*np.sin(2*np.pi*50*t) + 20*np.sin(2*np.pi*150*t)
N = len(signal)

# DFT
W         = 2*np.pi*np.outer(np.arange(N), np.arange(N))/N
dft_mag   = np.sqrt((np.cos(W)@signal)**2 + (np.sin(W)@signal)**2) / N
dft_phase = np.arctan2(np.sin(W)@signal, np.cos(W)@signal)

# Reconstruct
re_sig = (dft_mag * np.cos(2*np.pi*np.arange(N)*50*t[:,None] + dft_phase)).sum(axis=1)

# Plot
plt.subplot(3,1,1); plt.plot(t, signal);        plt.title("Original")
plt.subplot(3,1,2); plt.bar(np.arange(N), dft_mag*2); plt.title("DFT Magnitude")
plt.subplot(3,1,3); plt.plot(t, -re_sig);       plt.title("Reconstructed")
plt.tight_layout(); plt.show()  