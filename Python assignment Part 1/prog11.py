#Write a Python program to count the number of characters (character frequency) in a string


string = "Yolo Life"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")