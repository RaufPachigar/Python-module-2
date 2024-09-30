#Write a Python script to concatenate following dictionaries to create a new one.
def concatenate_dicts(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print(concatenate_dicts(dict1, dict2))