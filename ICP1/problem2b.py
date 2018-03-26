from math import fmod

number_1 = float(input("Enter first number: "))

number_2 = float(input("Enter second number: "))

if number_2 == 0:
    print('You cannot divide by zero')
else:
    quotient = number_1/number_2
    print(quotient)

    remainder = number_1%number_2
    print(remainder)



