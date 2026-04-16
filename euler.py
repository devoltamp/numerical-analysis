# import pdb
# Euler's Method for dy/dx = x + y

x = 0.0
y = 1.0
h = 0.1
steps = 50

for i in range(steps):
    slope = x + y
    y = y + h * slope
    x = x + h # increment in x
    print(f"x = {x:.2f}, y = {y:.6f}")
