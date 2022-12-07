start, moves = open("input.txt").read().split("\n\n")

stacks = [[] for _ in range(9)]
for line in reversed(start.split("\n")):
    for i in range(9):
        c = line[1 + 4 * i]
        if c.isalpha():
            stacks[i].append(c)

if __name__ == "__main__":
    for line in moves.split("\n"):
        n, start, end = map(int, line.split()[1::2])
        for _ in range(n):
            c = stacks[start - 1].pop()
            stacks[end - 1].append(c)

    for stack in stacks:
        print(stack.pop(), end="")
    print()
