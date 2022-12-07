from shared import stacks, moves

for line in moves.split("\n"):
    n, start, end = map(int, line.split()[1::2])
    crates = stacks[start - 1][-n:]
    stacks[start - 1] = stacks[start - 1][:-n]
    stacks[end - 1].extend(crates)

for stack in stacks:
    print(stack.pop(), end="")
print()
