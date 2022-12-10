lines = open("input.txt").read().split("\n")

i = total_strength = 0
adding = False
cycle = x = 1
while i < len(lines):
    cycle += 1
    if lines[i] == "noop":
        i += 1
    elif adding:
        adding = False
        x += int(lines[i].split()[1])
        i += 1
    else:
        adding = True

    if cycle in [20, 60, 100, 140, 180, 220]:
        total_strength += cycle * x

print(total_strength)
