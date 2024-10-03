#Write a Python program to read an entire text file

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

read_file('example.txt')
