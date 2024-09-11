#Write a Python program to count the number of strings
#where the string length is 2 or more and the first and last character are same from a given list of strings.

list_string=['apple', 'banana', 'cherry', 'date', 'elderberry', 'aba', 'adda', 'ajja']

def count_string(list):
    count=0

    for i in list:
        if len(i) > 2 and i[0] == i[-1] :
            count += 1

    print(f"{count}  strings in the given list has length more than 2 and the first and last character are same")

count_string(list_string)
