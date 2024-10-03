#Can one block of except statements handle multiple exception

# Yes, multiple exceptions can be handled in a single except statement by using a tuple.


try:
    result = 10 / 0
except (ZeroDivisionError, ValueError):
    print("Error occurred!")