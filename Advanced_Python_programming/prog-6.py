#Write a Python program to read a file line by line and store it into a list

def file_to_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

lines = file_to_list('example.txt')
print(lines)
