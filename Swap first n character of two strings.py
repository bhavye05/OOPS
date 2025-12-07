s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
n = int(input("Enter n: "))

new1 = s2[:n] + s1[n:]
new2 = s1[:n] + s2[n:]

print(new1)
print(new2)
