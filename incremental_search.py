# code is still buggy and won't give the correct root

def f(x):
    return x**3 - 4*x - 9

guess = float(input("Enter the initial guess: "))
tolerance = 0.01
max_iter = 100

x = guess
iteration = 0

while iteration < max_iter:
    fx = f(x)

    if abs(fx) < tolerance:
        print(f"Root : x = {x:.4f}")
        break
        # here the code will break if the iteration will exceed it's own limitation

    if fx > 0:
        x = x - 0.1
    else:
        x = x + 0.1

    iteration = iteration + 1

else:
    print("root not found")
