from shared import sizes

total = sum(filter(lambda size: size <= 100000, sizes))

print(total)
