from itertools import chain
from shared import sensors, dist


def perimiter(x, y, r):
    nw = ((x - r - 1 + i, y - i) for i in range(r + 1))
    ne = ((x + i, y - r - 1 + i) for i in range(r + 1))
    se = ((x + r + 1 - i, y + i) for i in range(r + 1))
    sw = ((x - i, y + r + 1 - i) for i in range(r + 1))
    return chain(nw, ne, se, sw)


def in_bounds(pos):
    x, y = pos
    return 0 <= x <= 4000000 and 0 <= y <= 4000000


boundary = chain(*(perimiter(sx, sy, r) for (sx, sy), r in sensors))
for pos in filter(in_bounds, boundary):
    for sensor, r in sensors:
        if dist(sensor, pos) <= r:
            break
    else:
        break

x, y = pos
print(4000000 * x + y)
