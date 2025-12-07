rows = int(input("Enter rows: "))

# Pyramid
for i in range(1, rows+1):
    print("*" * i)

# Reverse pyramid
for i in range(rows, 0, -1):
    print("*" * i)
