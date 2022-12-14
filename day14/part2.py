from shared import solid, move


def simulate(solid):
    x, y = 500, 0
    to = move(x, y, solid)
    while to is not None:
        x, y = to
        to = move(x, y, solid)
    solid.add((x, y))
    return y > 0


count = 0
while simulate(solid):
    count += 1

print(count + 1)
