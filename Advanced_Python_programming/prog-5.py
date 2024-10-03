#Write a Python program to read last n lines of a file.

from collections import deque

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = deque(file, n)
        for line in lines:
            print(line, end='')

read_last_n_lines('example.txt', 3)
