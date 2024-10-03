#How many except statements can a try-except block have? Name Some built-in exception classes



# A try block can have multiple except blocks to handle different exceptions.



try:
    x = int(input())
except ValueError:
    print("Value Error!")
except ZeroDivisionError:
    print("Division by Zero!")
    
    
    
# Some built-in exception classes:
# ValueError
# ZeroDivisionError
# TypeError
# FileNotFoundError
# IndexError