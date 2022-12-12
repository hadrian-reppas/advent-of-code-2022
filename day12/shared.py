inp = open("input.txt").read()
grid = [list(line) for line in inp.split("\n")]
rows, cols = len(grid), len(grid[0])

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "S":
            start = row, col
            grid[row][col] = "a"
        elif grid[row][col] == "E":
            end = row, col
            grid[row][col] = "z"


def can_move(a, b):
    return ord(b) - ord(a) <= 1
