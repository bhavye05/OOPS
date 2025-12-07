lst = [1,2,3,4,5,6,7,8]
cubes = []

for x in lst:
    if isinstance(x, int) and x % 2 == 0:
        cubes.append(x**3)

print(cubes)
