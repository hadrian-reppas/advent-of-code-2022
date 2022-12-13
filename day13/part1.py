from shared import less_than

inp = open("input.txt").read()

total = 0
for i, pair in enumerate(inp.split("\n\n")):
    a, b = map(eval, pair.split("\n"))
    if less_than(a, b):
        total += i + 1

print(total)
