#Write a Python function to get the largest number, smallest num and sum of all from a list.

def num(ls):
    largest_num=0

    for i in ls:
        if i > largest_num:
            largest_num = i

    for i in ls:
        if i < ls[0]:
            ls[0] = i
    print("largest number in the list is ",largest_num)
    print("smallest number in the list is ",ls[0])


ls=[5,8,7,9,69,54,87,36,54,25,1,4,8]
num(ls)

