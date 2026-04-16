import numpy as np
import matplotlib.pyplot as plt

# to get the random digits
A = np.random.randint(0, 100, size=10)
B = np.random.randint(0, 100, size=10)
print(A)
print(B)

# to plot the sine wave
x = np.linspace(0, 2 * np.pi, 100) 
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("Angle (radians)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()