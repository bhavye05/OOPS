ch = input("Enter a character: ")

if ch.isalpha():
    print("Letter")
    if ch.isupper():
        print("Uppercase")
    else:
        print("Lowercase")

elif ch.isdigit():
    print("Digit")
    names = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
    print("Name:", names[int(ch)])

else:
    print("Special Character")
