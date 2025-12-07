def find_all(a, b):
    res = []
    start = 0
    while True:
        idx = a.find(b, start)
        if idx == -1:
            break
        res.append(idx)
        start = idx + 1
    return res if res else -1

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
print(find_all(s1, s2))
