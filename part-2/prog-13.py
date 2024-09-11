#Write a Python program to select an item randomly from a list
import random

def select(ls):
    random_item = random.choice(ls)
    return random_item


ls = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
random_item = select(ls)

print(random_item)
