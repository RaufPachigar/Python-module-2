#Write a Python program to find the repeated items of a tuple.

def find_repeated_items(tup):
    frequency = {}
    repeated_items = []
    
    for item in tup:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    for item, count in frequency.items():
        if count > 1:
            repeated_items.append(item)
    
    return repeated_items

tup = (1, 2, 3, 2, 4, 5, 5, 6, 2)
print("Original tuple:", tup)
print("Repeated items:", find_repeated_items(tup))