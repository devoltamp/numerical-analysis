# best bisection code!
def f(x):
    return x**3 - 16


def bisection(a, b):
    if f(a)*f(b) < 0:

        while True:
            c = (a + b) / 2

            if abs(f(c)) < tolerance:
                print("root: ", abs(c))
                return

            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
    else:
        print("out of limit")

# -------- main program --------
tolerance = 0.01
a = float(input("Enter the first guess: "))
b = float(input("Enter the second guess: "))

bisection(a, b)