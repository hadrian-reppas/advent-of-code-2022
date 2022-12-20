from shared import rocks, jet_is_left, fits, i


def top():
    max_y = max(y for _, y in solid)
    return frozenset((x, max_y - y) for x, y in solid if y >= max_y - 30)


solid = {(x, 0) for x in range(7)}
cache = {}
height = rock_index = surplus = 0
while rock_index < 1000000000000:
    x, y = 2, height + 4
    rock = rocks[rock_index % 5]
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

            info = rock_index % 5, top(), i
            if info in cache:
                old_rock_index, old_height = cache[info]
                time = rock_index - old_rock_index
                rate = (1000000000000 - rock_index) // time
                surplus += rate * (height - old_height)
                rock_index += rate * time
            cache[info] = rock_index, height
            break
        y -= 1
    rock_index += 1

print(height + surplus)
