start, moves = open("input.txt").read().split("\n\n")
moves = moves.split("\n")

stacks = [[] for _ in range(9)]
for line in reversed(start.split("\n")):
    for i in range(9):
        c = line[1 + 4 * i]
        if c.isalpha():
            stacks[i].append(c)
