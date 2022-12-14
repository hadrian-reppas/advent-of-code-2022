def move(x, y, solid):
    if y == max_y + 1:
        return None
    elif (x, y + 1) not in solid:
        return (x, y + 1)
    elif (x - 1, y + 1) not in solid:
        return (x - 1, y + 1)
    elif (x + 1, y + 1) not in solid:
        return (x + 1, y + 1)


solid = set()
for line in open("input.txt").read().split("\n"):
    coords = line.split(" -> ")
    px, py = map(int, coords.pop().split(","))
    while coords:
        x, y = map(int, coords.pop().split(","))
        if x == px:
            for sy in range(min(y, py), max(y, py) + 1):
                solid.add((x, sy))
        else:
            for sx in range(min(x, px), max(x, px) + 1):
                solid.add((sx, y))
        px, py = x, y

max_y = max(y for _, y in solid)
