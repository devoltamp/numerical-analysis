def f(x):
    return x**2 - 16

def falsep(a, b):
    if f(a) * f(b) < 0:
        while True:
            c = b - ((f(b)*(a-b))/(f(a)-f(b)))

            if abs(f(c)) < tolerance:
                print("root: ", c)
                return
            
            if f(a)*f(c) < 0:
                b = c
            elif f(c)*f(b) < 0:
                a = c
            else:
                pass
            # the loop can be anything
    else:
        print("out of limit")

tolerance = 0.01
a = float(input("a = "))
b = float(input("b = "))
falsep(a, b)

