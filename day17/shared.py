jets = open("input.txt").read()
i = 0


def jet_is_left():
    global i
    result = jets[i] == "<"
    i = (i + 1) % len(jets)
    return result


rocks = [
    lambda x, y: {(x, y), (x + 1, y), (x + 2, y), (x + 3, y)},
    lambda x, y: {
        (x + 1, y),
        (x, y + 1),
        (x + 1, y + 1),
        (x + 2, y + 1),
        (x + 1, y + 2),
    },
    lambda x, y: {(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)},
    lambda x, y: {(x, y), (x, y + 1), (x, y + 2), (x, y + 3)},
    lambda x, y: {(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)},
]


def fits(rock, solid):
    if any(x < 0 for x, _ in rock) or any(x >= 7 for x, _ in rock):
        return False
    return not rock & solid
