from shared import sensors, beacons, dist

min_x = min(x - r for (x, _), r in sensors)
max_x = max(x + r for (x, _), r in sensors)

count = 0
for x in range(min_x, max_x + 1):
    if (x, 2000000) in beacons:
        continue
    for sensor, r in sensors:
        if dist((x, 2000000), sensor) <= r:
            count += 1
            break

print(count)
