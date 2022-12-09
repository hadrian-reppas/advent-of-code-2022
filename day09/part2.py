from shared import new_tail

inp = open("input.txt").read()
moves = [(line[0], int(line[2:])) for line in inp.split("\n")]

rope = [[0, 0] for _ in range(10)]
visited = {(0, 0)}
for direction, n in moves:
    for _ in range(n):
        if direction == "U":
            rope[0][1] += 1
        elif direction == "D":
            rope[0][1] -= 1
        elif direction == "R":
            rope[0][0] -= 1
        else:
            rope[0][0] += 1
        for i in range(9):
            rope[i + 1] = new_tail(rope[i], rope[i + 1])
        visited.add(tuple(rope[9]))

print(len(visited))
