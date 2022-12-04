inp = open("input.txt").read()

lines = inp.split("\n")
total = 0
while lines:
    a, b, c, *lines = lines
    overlap, = set(a) & set(b) & set(c)
    if overlap.islower():
        total += ord(overlap) - ord("a") + 1
    else:
        total += ord(overlap) - ord("A") + 27

print(total)
