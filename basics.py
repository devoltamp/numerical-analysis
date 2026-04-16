import math
import time

# # variables
# price=10.99
# gpa=3.2
#
# print(f"the price is: ${price}")
# print(f"your gpa is: {gpa}")
#
# # boolean
# for_sale=False
#
# if for_sale:
#     print("that item is for sale")
# else:
#     print("that item is not available")
#
#
# # Typecasting
# name="bro code"
# age=25
# gpa=3.2
# is_student=True
#
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))
#
# gpa=int(gpa)
# print(gpa)
#
#
# # combining diffrent string together
# age=str(age)
# age += "1"
# print(age)
#
# name=bool(name) #to check whether the variable is empty or what!
# print(name)
#
#
# # input() >> the output will be always in the string
# name=input("what is your name? ")
# age=input("how old are you? ")
#
# print(f"Hello {name}")
# print("Happy Birthday")
# age = int(age) + 1
# print(f"you are {age} years old")

# # example >> shopping cart programm
# item = input("which item? ")
# price = float(input("price? "))
# quantity = int(input("quantity? "))
#
# total = price * quantity
#
# print(f"you have bought {quantity} * {item}/s")
# print(f"your total is: ${total}")


# # to calculate the circumference
# radius = float(input("Enter the radius: "))
# circumference = 2 * math.pi * radius  #always have to give the path to the library
# print(f"The circumference is: {round(circumference, 2)}cm")


# # if statememt
# age = int(input("Enter your age: "))
# if age >= 100:
#     print("you are too old to sign up")

# elif age<0:
#     print("you haven't been born yet")

# elif age>=18:
#     print("you are signed up!")

# else:
#     print("hello there mf!")

# # to check whether the name is written or what
# name = input("Enter your name: ")
# if name == "":
#     print("you did not actually type in the name!!")
# else:
#     print(f"Hello {name}")


# # python calculator simple one
# print("The simplest calculator to mankind")
# operator = input("Enter an operator (+ - *)")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if operator == "+":
# 	result = num1 + num2
# 	print(result)
# elif operator == "-":
# 	result = num1 - num2
# 	print(result)
# elif operator == "*":
# 	result = num1 * num2
# 	print(result)
# elif operator == "/":
# 	result = num1 / num2
# 	print(result)
# else:
# 	print(f"{operator} is not a valid operator")


# conditional expressions (ternary operator)

# # num = 6
# num = int(input("Enter a number: "))
# result = "even" if num%2 == 0 else "odd"
# print(result)

# age = int(input("Enter your age: "))
# status = "Adult" if age >=18 else "Child"
# print(status)


# username = input("Enter your username: ")

# if len(username) > 12:
# 	print("your username can't be more than 12 characters!")
# elif not username.find(" ") == -1:
# 	print("your username can't contain spaces!")
# elif not username.isalpha():
# 	print("your username can't contain numbers!")
# else:
# 	print(f"welcome {username}")


# # indexing the string
# credit_number = "1234-5678-9012-3456"
# print(credit_number[0])
# print(credit_number[::]) # this will just print the whole string
# print(credit_number[-1])
# print(credit_number[::3])


# num = input("Enter a number: ")
# s = len(num)


# # format specirfier
# price1 = 3000.3434343
# price2 = -9870.65
# price3 = 1200.34

# print(f"price 1 is ${price1:+5}")
# print(f"price 2 is ${price2:+5}")
# print(f"price 3 is ${price3:+5}")

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter a name!")
#     # name = input("Enter your name: ")
#     break
# print(f"howdy {name}")


# food = input("Enter a food you like: ")

# while not food == "q": # to exit the command comepletely 
#     print(f"you like {food}")
#     food = input("Enter an another food you like: ")

# print("bye")


# # Compound interest calculator

# principle = 0
# rate = 0
# time = 0

# # while True:
# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("principle can't be less than or equal to zero")

# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("interest rate can't be less than or equal to zero")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("time can't be less than or equal to zero")


# total = principle * pow((1 + rate/100), time)
# print(f"Balance after {time} years: {total:,.2f}")

# interest_value = total - principle
# print(f"The interest value: {interest_value:,.2f}")

# per_month = (interest_value/time) / 12 
# print(f"Per month installment: {per_month:,.2f}")
# print("Have a good time paying the loan >> you sucker")


# # backward counter with the time included

# # nope = 1000%60
# # print(nope)

# my_time = int(input("Enter time in seconds: "))

# for x in range(my_time, 0, -1): 
#     seconds = int(x % 60)
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600) % 24
#     # days = int( x / 86400) % 365
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("time's up!")


# # nested loops
# num = int(input("Enter the number that you want to iterate: "))
# for x in range(num):
#     for y in range(1, num):
#         print(y, end=" ")
#     print()

fruits = ["apple", "orange", "banana", "coconut"]

for fruit in fruits:
    print(fruit, end=" ")
    # print(help(fruits))
    

