from collections import Counter

lines = open("input.txt").read().split("\n")
elves = set()
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c == "#":
            elves.add((col, len(lines) - row - 1))

moves = [
    lambda x, y: ((x, y + 1), {(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)}),
    lambda x, y: ((x, y - 1), {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)}),
    lambda x, y: ((x - 1, y), {(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)}),
    lambda x, y: ((x + 1, y), {(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)}),
]

neighbors = lambda x, y: {
    (x + 1, y),
    (x + 1, y + 1),
    (x, y + 1),
    (x - 1, y + 1),
    (x - 1, y),
    (x - 1, y - 1),
    (x, y - 1),
    (x + 1, y - 1),
}


def step(elves, i):
    proposed = {}
    counts = Counter()
    for x, y in elves:
        if not neighbors(x, y) & elves:
            proposed[(x, y)] = (x, y)
            continue
        for d in range(4):
            prop, area = moves[(i + d) % 4](x, y)
            if not area & elves:
                proposed[(x, y)] = prop
                counts[prop] += 1
                break
        else:
            proposed[(x, y)] = (x, y)
    new_elves = set()
    for old, new in proposed.items():
        if counts[new] == 1:
            new_elves.add(new)
        else:
            new_elves.add(old)
    return new_elves
