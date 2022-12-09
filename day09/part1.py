from shared import new_tail

inp = open("input.txt").read()
moves = [(line[0], int(line[2:])) for line in inp.split("\n")]

head = tail = (0, 0)
visited = {(0, 0)}
for direction, n in moves:
    for _ in range(n):
        if direction == "U":
            head = head[0], head[1] + 1
        elif direction == "D":
            head = head[0], head[1] - 1
        elif direction == "R":
            head = head[0] + 1, head[1]
        else:
            head = head[0] - 1, head[1]
        tail = new_tail(head, tail)
        visited.add(tail)

print(len(visited))
