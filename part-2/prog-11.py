#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def listfilter(ls):

    unique_set=set(ls)

    unique_list=list(unique_set)

    return unique_list



ls=[2,5,4,2,1,5,4,8,9,8,7,6,5,7,8]

unique_list=listfilter(ls)

print(unique_list)