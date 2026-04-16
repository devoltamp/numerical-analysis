# i wrote it but it does not work at all (it sucks!!)
# it's not that advance

def f(x):
    return x**2 - 16

def update_variable(a,b,c,fa,fb,fc):
    if abs(fc) < tolerence:
        j=1
    else:
        j=0
        if fa * fc < 0:
            b=c
        elif fc * fb < 0:
            a=c
        else:
            pass

    return a,b,c,j

tolerence = 0.001
a = float(input("Enter the first guess: "))
b = float(input("Enter the second guess: "))

while True:
    fa = f(a)
    fb = f(b)
    c = (a+b)/2
    fc = f(c)

    uv = update_variable(a,b,c,fa,fb,fc)



    if uv[3] > 0:
        print(abs(uv[2]))
        break
    else:
        a=a
        b=b
