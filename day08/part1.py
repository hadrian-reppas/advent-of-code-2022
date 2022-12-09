inp = open("input.txt").read()
forest = [list(map(int, line)) for line in inp.split("\n")]
rows, cols = len(forest), len(forest[0])

visible = [[False] * cols for _ in range(rows)]

for row in range(rows):
    max_height = -1
    for col in range(cols):
        if forest[row][col] > max_height:
            max_height = forest[row][col]
            visible[row][col] = True
    max_height = -1
    for col in reversed(range(cols)):
        if forest[row][col] > max_height:
            max_height = forest[row][col]
            visible[row][col] = True

for col in range(cols):
    max_height = -1
    for row in range(rows):
        if forest[row][col] > max_height:
            max_height = forest[row][col]
            visible[row][col] = True
    max_height = -1
    for row in reversed(range(rows)):
        if forest[row][col] > max_height:
            max_height = forest[row][col]
            visible[row][col] = True

visible_count = sum(sum(line) for line in visible)
print(visible_count)
