# Task 2:
# Using the Math Module for Calculations
import math


def square_root(n):
    if n < 0:
        return "not defined"
    return math.sqrt(n)


def natural_logarithm(n):
    if n < 0:
        return "Logarithm is undefined for zero or negative numbers"
    return math.log(n)



def sine_of_the_number(n):
    if n < 0:
        return "not defined"
    return math.sin(n)
    # noinspection PyUnreachableCode
    math.radians(n)

# take input from user
num = int(input("Enter a non-negative integer: "))

# Call the function and print the result
print(f"The square root of {num} is {square_root(num)}")

print(f"The natural logarithm of{num} is {natural_logarithm(num)}")

print(f"The sine of {num} is {sine_of_the_number(num)}")