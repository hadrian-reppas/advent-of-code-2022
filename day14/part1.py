from shared import solid, max_y, move


def simulate(solid):
    x, y = 500, 0
    to = move(x, y, solid)
    while to is not None and y < max_y:
        x, y = to
        to = move(x, y, solid)
    solid.add((x, y))
    return to is None


count = 0
while simulate(solid):
    count += 1

print(count)
