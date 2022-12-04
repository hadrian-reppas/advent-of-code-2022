inp = open("input.txt").read()

total = 0
for line in inp.split("\n"):
    left, right = line[:len(line)//2], line[len(line)//2:]
    overlap, = set(left) & set(right)
    if overlap.islower():
        total += ord(overlap) - ord("a") + 1
    else:
        total += ord(overlap) - ord("A") + 27

print(total)
