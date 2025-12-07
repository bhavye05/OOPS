s = input("Enter a string: ")
ch = input("Enter a character: ")
rep = input("Enter replacement character: ")

# a) Frequency
print("Frequency:", s.count(ch))

# b) Replace a char
print("Replace:", s.replace(ch, rep, 1))

# c) Remove first occurrence
print("After removing first:", s.replace(ch, "", 1))

# d) Remove all occurrences
print("After removing all:", s.replace(ch, ""))
