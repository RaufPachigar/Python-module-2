#Write a Python program to check multiple keys exists in a dictionary

def multiple_keys_exist(dict, keys):
    return all(key in dict for key in keys)

d = {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'b', 'c']

print( multiple_keys_exist(d, keys))