def my_function(a,b):
    f_a = a**2 - 16
    f_b = b**2 - 16
    c = b - ((f_b*(a-b))/(f_a-f_b))
    f_c = c**2 - 16
    return f_a, f_b, f_c, c

def update_variable(a,b,c,f_a,f_b,f_c):
    if abs(f_c) < tolerence:
        j = 1
    else:
        j = 0
        if f_a * f_c < 0:
            b=c
        elif f_c * f_b < 0:
            a=c
        else:
            # a=a
            # b=b
            # c=c
            pass
    return a,b,c,j

tolerence = 0.01
a = float(input("Enter the first guess: "))
b = float(input("Enter the second guess: "))

while True:
    z = my_function(a,b)
    m = update_variable(a,b,z[3],z[0],z[1],z[2])

    if m[3] > 0:
        print(f"The root is: {m[2]}")
        break
    else:
        a = m[0]
        b = m[1]
