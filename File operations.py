file = "data.txt"

with open(file) as f:
    lines = f.readlines()

text = "".join(lines)

# a) Count
print("Characters:", len(text))
print("Words:", len(text.split()))
print("Lines:", len(lines))

# b) Frequency
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("Character frequency:", freq)

# c) Words in reverse
words = text.split()
print("Reverse words:", words[::-1])

# d) Even/Odd lines
with open("File1.txt","w") as f1, open("File2.txt","w") as f2:
    for i, line in enumerate(lines):
        if (i+1) % 2 == 0:
            f2.write(line)
        else:
            f1.write(line)
