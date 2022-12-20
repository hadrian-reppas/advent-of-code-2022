cells = set()
for line in open("input.txt").read().split("\n"):
    cells.add(eval(line))

surface_area = 0
for x, y, z in cells:
    surface_area += (x + 1, y, z) not in cells
    surface_area += (x - 1, y, z) not in cells
    surface_area += (x, y + 1, z) not in cells
    surface_area += (x, y - 1, z) not in cells
    surface_area += (x, y, z + 1) not in cells
    surface_area += (x, y, z - 1) not in cells

print(surface_area)
