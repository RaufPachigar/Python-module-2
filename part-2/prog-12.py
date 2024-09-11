#Write a Python program to convert a list of characters into a string.


def ListToString(ls):

    result = ''.join(ls)

    return result

ls=['r','a','u','f']
string=ListToString(ls)

print(string)