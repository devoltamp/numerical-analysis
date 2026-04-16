# bisection method
# the long code

def my_function(a,b,c):
    f_a = a**2 - 16
    f_b = b**2 - 16
    f_c = c**2 - 16
    return f_a, f_b, f_c


def update_root(a,b,c,f_a,f_b,f_c):
    if abs(f_c) < tolerence:
        j=1
    else:
        j=0
        if f_a * f_c < 0:
            a=a
            b=c
        elif f_c * f_b < 0:
            a=c
            b=b
        else:
            a=a
            b=b
            c=c
    return a,b,c,j


# the beginning
tolerence = 0.01

a = float(input("Enter the first guess: "))
b = float(input("Enter the second guess: "))

# initial_guess = [3, 7]
# a = initial_guess[0]
# b = initial_guess[1]

while True:
    c = (a+b)/2
    z = my_function(a,b,c)
    m = update_root(a,b,c,z[0],z[1],z[2])

    if m[3] > 0: # m[3] = j (always the  return values would be counted)
        print(abs(m[2]))
        break
    else:
        a = m[0]
        b = m[1]