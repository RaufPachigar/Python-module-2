#Write a Python program to read a file line by line store it into a variable.

def file_to_string(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

content = file_to_string('example.txt')
print(content)
