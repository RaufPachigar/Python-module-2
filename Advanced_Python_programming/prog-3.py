#Write a Python program to append text to a file and display the text

def append_text(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
    with open(filename, 'r') as file:
        print(file.read())

append_text('example.txt', '\nNew text appended.')
