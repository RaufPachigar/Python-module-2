#Write a Python program to map two lists into a dictionary



def map_lists_to_dict(keys, values):
    return dict(zip(keys, values))

keys = ['a', 'b', 'c']
values = [1, 2, 3]


print( map_lists_to_dict(keys, values))