# Write a Python program to get the Fibonacci series of given range.

def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

number = int(input("Enter a number to generate Fibonacci series up to that number: "))

result = fibonacci_series(number)
print(f"Fibonacci series up to {number} is: {result}")
