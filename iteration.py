# iteration method
def f(x):
    return x**3 - 4*x - 9

guess = -5
tolerance = 0.01

while True:
    x = guess
    fx = f(x)

    if abs(fx) < tolerance:
        print(f"root: x = {x:.4f}")
        break

    elif fx > 0:
        x = x - 0.1
    else:
        x = x + 0.1


print("root not found within iteration limit")
