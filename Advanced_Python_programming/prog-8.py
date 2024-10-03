#Write a python program to find the longest words.

def find_longest_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    longest_word = max(words, key=len)
    return longest_word

print(find_longest_words('example.txt'))
