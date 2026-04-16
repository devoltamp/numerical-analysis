# just go with the flow
def f(x):
    return x**2 - 16

tolerence = 0.001

x0 = float(input("Enter the first guess: "))
x1 = float(input("Enter the second guess: "))

while True:
    f0 = f(x0)
    f1 = f(x1)

    if f1 - f0 == 0:
        print("devision by zero method fails")
        break

    x2 = x1 - f1*((x1-x0)/(f1-f0))

    if abs(x2-x1) < tolerence:
        print(f"root: {x2}")
        break

    x0 = x1
    x1 = x2
