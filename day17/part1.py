from shared import rocks, jet_is_left, fits

j = 0


def next_rock():
    global j
    result = rocks[j]
    j = (j + 1) % 5
    return result


solid = {(x, 0) for x in range(7)}
height = 0
for _ in range(2022):
    x, y = 2, height + 4
    rock = next_rock()
    while True:
        if jet_is_left():
            if fits(rock(x - 1, y), solid):
                x -= 1
        else:
            if fits(rock(x + 1, y), solid):
                x += 1

        if rock(x, y - 1) & solid:
            solid.update(rock(x, y))
            height = max(height, max(y for _, y in rock(x, y)))
            break
        y -= 1

print(height)
