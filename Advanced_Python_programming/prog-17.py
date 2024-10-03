#When is the finally block executed

# the finally block is always executed, whether an exception occurs or not.
# It's used to clean up resources like closing files or database connections.


try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file.")
    file.close()