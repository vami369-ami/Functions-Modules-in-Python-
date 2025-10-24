# Task 1:
# Function to Calculate Factorial Using loop

def factorial (n):
    if n < 0:
        return "Factorial cannot be negative"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from the user
num = int(input("Enter a non-negative integer: "))

# Call the function and print the result
print(f"The factorial of {num} is {factorial(num)}")



