def dist(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)


sensors = []
beacons = set()
for line in open("input.txt").read().split("\n"):
    lhs, rhs = line.split(":")
    _, sx, sy = lhs.split("=")
    sensor = (int(sx[:-3]), int(sy))
    _, bx, by = rhs.split("=")
    beacon = (int(bx[:-3]), int(by))
    beacons.add(beacon)
    sensors.append((sensor, dist(beacon, sensor)))
