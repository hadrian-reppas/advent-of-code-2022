cells = set()
for line in open("input.txt").read().split("\n"):
    cells.add(eval(line))

min_x = min(x for x, _, _ in cells) - 1
max_x = max(x for x, _, _ in cells) + 1
min_y = min(y for _, y, _ in cells) - 1
max_y = max(y for _, y, _ in cells) + 1
min_z = min(z for _, _, z in cells) - 1
max_z = max(z for _, _, z in cells) + 1

seen = set()
stack = [(min_x, min_y, min_z)]
while stack:
    x, y, z = stack.pop()
    if (x, y, z) in seen:
        continue
    seen.add((x, y, z))
    if x > min_x and (x - 1, y, z) not in cells:
        stack.append((x - 1, y, z))
    if x < max_x and (x + 1, y, z) not in cells:
        stack.append((x + 1, y, z))
    if y > min_y and (x, y - 1, z) not in cells:
        stack.append((x, y - 1, z))
    if y < max_y and (x, y + 1, z) not in cells:
        stack.append((x, y + 1, z))
    if z > min_z and (x, y, z - 1) not in cells:
        stack.append((x, y, z - 1))
    if z < max_z and (x, y, z + 1) not in cells:
        stack.append((x, y, z + 1))

surface_area = 0
for x, y, z in cells:
    surface_area += (x + 1, y, z) in seen
    surface_area += (x - 1, y, z) in seen
    surface_area += (x, y + 1, z) in seen
    surface_area += (x, y - 1, z) in seen
    surface_area += (x, y, z + 1) in seen
    surface_area += (x, y, z - 1) in seen

print(surface_area)
