# Write a Python program to remove duplicates from a list.

ls=[2,5,4,2,8,8,5,7,4,9,8,3]


def rem(ls):
    new_list=[]
    for i in ls :
        if i not in new_list:
            new_list.append((i))
    print(new_list)

rem(ls)