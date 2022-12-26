from shared import elves, step

count = 0
while True:
    new_elves = step(elves, count)
    if new_elves == elves:
        break
    elves = new_elves
    count += 1

print(count + 1)
