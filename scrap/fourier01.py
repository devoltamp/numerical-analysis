import numpy as np
import matplotlib.pyplot as plt

def fourier_series(x, func, n_terms):
    """
    Approximate a function using Fourier Series up to n_terms harmonics.
    Works on the interval [-pi, pi].
    """
    L = np.pi  # half-period
    a0 = (1 / L) * np.trapz(func(x), x)
    approximation = a0 / 2

    for n in range(1, n_terms + 1):
        an = (1 / L) * np.trapz(func(x) * np.cos(n * x / L), x)
        bn = (1 / L) * np.trapz(func(x) * np.sin(n * x / L), x)
        approximation += an * np.cos(n * x / L) + bn * np.sin(n * x / L)

    return approximation

# --- Define some common waveforms ---

def square_wave(x):
    return np.sign(np.sin(x))

def sawtooth_wave(x):
    return (x % (2 * np.pi) - np.pi) / np.pi

def triangle_wave(x):
    return 2 * np.abs(2 * (x / (2 * np.pi) - np.floor(x / (2 * np.pi) + 0.5))) - 1

# --- Plot ---

x = np.linspace(-np.pi, np.pi, 1000)
terms_to_show = [1, 3, 5, 15]
func = square_wave  # change this to sawtooth_wave or triangle_wave

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Fourier Series Approximation — Square Wave", fontsize=14)

for ax, n in zip(axes.flat, terms_to_show):
    approx = fourier_series(x, func, n)
    ax.plot(x, func(x), 'k--', linewidth=1, label='Original', alpha=0.5)
    ax.plot(x, approx, 'b-', linewidth=1.5, label=f'{n} terms')
    ax.set_title(f'N = {n}')
    ax.legend(fontsize=9)
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("fourier_series.png", dpi=150)
plt.show()