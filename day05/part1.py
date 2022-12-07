from shared import stacks, moves

for line in moves:
    n, start, end = map(int, line.split()[1::2])
    for _ in range(n):
        c = stacks[start - 1].pop()
        stacks[end - 1].append(c)

for stack in stacks:
    print(stack.pop(), end="")
print()
