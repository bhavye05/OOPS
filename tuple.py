t1 = (1,2,5,7,9,2,4,6,8,10)

# a) half values
mid = len(t1)//2
print(t1[:mid])
print(t1[mid:])

# b) only even numbers
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print(even_tuple)

# c) concatenate
t2 = (11,13,15)
print(t1 + t2)

# d) max and min
print("Max:", max(t1))
print("Min:", min(t1))
