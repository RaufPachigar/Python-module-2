#Write a Python program to read first n lines of a file.


def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        for _ in range(n):
            print(file.readline(), end='')

read_first_n_lines('example.txt', 3)
