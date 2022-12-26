import re

field, directions = open("input.txt").read().split("\n\n")
lines = field.split("\n")
maze = [[None] * 150 for _ in range(200)]
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c != " ":
            maze[row][col] = c == "."

matches = re.findall(r"\d*[LRX]", directions + "X")
path = [(int(m[:-1]), m[-1]) for m in matches]

turn_map = {
    "R": [1, 2, 3, 0],
    "X": [0, 1, 2, 3],
    "L": [3, 0, 1, 2],
}


def get_password(move):
    row = facing = 0
    col = maze[0].index(True)

    for n, turn in path:
        for _ in range(n):
            row, col, facing = move(row, col, facing)
        facing = turn_map[turn][facing]

    return 1000 * (row + 1) + 4 * (col + 1) + facing
