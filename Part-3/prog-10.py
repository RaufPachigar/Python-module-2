
#Write a Python program to print all unique values in a dictionary

def print_unique_values(d):
    unique_values = set(d.values())
    for value in unique_values:
        print(value)

d = {'a': 100, 'b': 200, 'c': 300, 'd': 200, 'e': 100}

print_unique_values(d)