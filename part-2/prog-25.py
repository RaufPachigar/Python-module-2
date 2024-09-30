#Write a Python program to remove an empty tuple(s) from a list of tuples


def remove_empty_tuples(tuples_list):
    return [t for t in tuples_list if t]

# Test the function
tuples_list = [(1, 2, 3), (), (4, 5, 6), (), (7, 8, 9)]
print(remove_empty_tuples(tuples_list))