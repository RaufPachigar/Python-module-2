#Write a Python program to get the Factorial number of given number.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

number = int(input("Enter a number: "))

result = factorial(number)
print(f"The factorial of {number} is {result}.")
