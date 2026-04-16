# the goat
def f(x):
    return x**2 - 16

def df(x):
    return 2*x


tolerence = 0.001
x = float(input("Enter the initial guess: "))

while True:
    fx = f(x)
    dfx = df(x)

    # not that important but still
    if dfx == 0:
        print("derivative is ZERO")
        break

    x_new = x - fx/dfx
    if abs(x_new - x) < tolerence:
        print(f"root: {abs(x_new)}")
        break

    x = x_new # this part is little bit confusing
