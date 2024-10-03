#Write a Python program to count the number of lines in a text file


def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())

print(count_lines('example.txt'))
