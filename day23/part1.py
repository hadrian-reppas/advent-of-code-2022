from shared import elves, step

for i in range(10):
    elves = step(elves, i)

min_x = min(x for x, _ in elves)
max_x = max(x for x, _ in elves)
min_y = min(y for _, y in elves)
max_y = max(y for _, y in elves)

area = (max_x - min_x + 1) * (max_y - min_y + 1)
print(area - len(elves))
