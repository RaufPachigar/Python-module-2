# Write a Python program to create a tuple with different data types.

my_tuple = (42, 3.14, "Hello, World!", True, [1, 2, 3], {'key': 'value'})

print("Tuple with different data types:")
print(my_tuple)

print("\nTypes of elements in the tuple:")
for element in my_tuple:
    print(f"{element}: {type(element)}")