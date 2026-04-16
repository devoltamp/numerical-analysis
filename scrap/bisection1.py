# not this one

def my_function(x1,x2,x3):
    # temp1 = x1**2 -4*x1 - 32
    # temp2 = x2**2 -4*x2 - 32
    # temp3 = x3**2 -4*x3 - 32

    temp1 = x1**3 - 16
    temp2 = x2**3 - 16
    temp3 = x3**3 - 16
    return temp1, temp2, temp3

def change_the_guess(a,b):
    a = -1*a
    b = b
    # a = a
    return a,b

def calculate(a,b):
    c = (a+b)/2
    [x1, x2, x3] = my_function(a,b,c)

    if abs(x3) < tolerence:
        print(c)
        residue = c**3 - 16
        print(abs(residue))
        j = 1
    elif x1 * x3 < 0:
        a = a
        b = c
        j = 0
    elif x3 * x2 < 0:
        a = c
        b = b
        j = 0
    else:
        j = 0
    return a,b,j


# def update_root(a,b,c,f_a,f_b,f_c):
#     if abs(f_c) < tolerence:
#         j=1
#     else:
#         j=0
#         if f_a * f_c < 0:
#             a=a
#             b=c
#         elif f_c * f_b < 0:
#             a=c
#             b=b
#         else:
#             a=a
#             b=b
#             c=c
#     return a,b,c,j



tolerence = 0.01
max_iteration = 5000
initial_guess = [10, -10]
# a = float(input("Enter the first guess: "))
# b = float(input("Enter the second guess: "))

# initial_guess = [3, 7]
a = initial_guess[0]
b = initial_guess[1]

v = my_function(a,b,0)
if v[0] * v[1] > 0:
    [a,b] = change_the_guess(a, b)
else:
    [a,b] = [a,b]
j = 0


# while True:
for i in range(0,max_iteration):

    # c = (a+b)/2
    # z = my_function(a,b,c)
    # m = update_root(a,b,c,z[0],z[1],z[2])
    #
    # if m[3] > 0:
    #     print(abs(m[2]))
    #     break
    # else:
    #     a = m[0]
    #     b = m[1]

    if j < 1:
        v = my_function(a,b,0)
        if v[0] * v[1] > 0:
            [a,b] = change_the_guess(a,b)
        else:
            [a,b] = [a,b]

        [a,b,j] = calculate(a,b)
        # print(a)
        # print(b)

    else:
        break
