#When will the else part of try-except-else be executed

# The else block is executed if no exception occurs in the try block.


try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("No error occurred!")