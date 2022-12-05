start, moves = open("input.txt").read().split("\n\n")

stacks = [[] for _ in range(9)]
for line in reversed(start.split("\n")):
    for i in range(9):
        c = line[1 + 4 * i]
        if c.isalpha():
            stacks[i].append(c)

for line in moves.split("\n"):
    n, start, end = map(int, line.split()[1::2])
    crates = stacks[start - 1][-n:]
    stacks[start - 1] = stacks[start - 1][:-n]
    stacks[end - 1].extend(crates)

for stack in stacks:
    print(stack.pop(), end="")
print()
