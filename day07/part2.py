from part1 import sizes

min_size = sizes[-1] - 40000000
best_size = min(filter(lambda size: size >= min_size, sizes))

print(best_size)
