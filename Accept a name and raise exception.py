name = input("Enter name: ")

try:
    if not name.isalpha():
        raise ValueError("Name contains digits or special characters")
    print("Valid name")
except ValueError as e:
    print(e)
