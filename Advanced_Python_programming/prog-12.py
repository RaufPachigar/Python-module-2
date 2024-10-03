#Write a Python program to copy the contents of a file to another file

def copy_file(src, dst):
    with open(src, 'r') as file1:
        content = file1.read()
    with open(dst, 'w') as file2:
        file2.write(content)

copy_file('example.txt', 'copy.txt')
