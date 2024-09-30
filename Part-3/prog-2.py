#Write a Python script to check if a given key already exists in a dictionary.

def key_exists(dict, key):
    return key in dict

d = {'a': 1, 'b': 2, 'c': 3}
key = 'b'

print( key_exists(d, key))