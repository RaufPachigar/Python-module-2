#Write a Python program to count the frequency of words in a file

from collections import Counter

def word_frequency(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return Counter(words)

print(word_frequency('example.txt'))

