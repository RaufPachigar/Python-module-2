#Write python program that user to enter only odd numbers, else will raise an exception.


def get_odd_number():
    try:
        num = int(input("Enter an odd number: "))
        if num % 2 == 0:
            raise ValueError("That is not an odd number!")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        print(f"Thank you, {num} is an odd number.")

get_odd_number()