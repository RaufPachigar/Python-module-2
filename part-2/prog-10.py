#Write a Python program to generate
# and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

squares=[x*2 for x in range(1,31)]

listA=squares[:5]  # first five ele
listB=squares[-5:] # last five ele

list = listA + listB

print(list)