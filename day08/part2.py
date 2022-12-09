inp = open("input.txt").read()
forest = [list(map(int, line)) for line in inp.split("\n")]
rows, cols = len(forest), len(forest[0])

scores = [[[] for _ in range(cols)] for _ in range(rows)]

for row in range(rows):
    visible = [None] * 10
    for col in range(cols):
        height = forest[row][col]
        if visible[height] is None:
            scores[row][col].append(col)
        else:
            scores[row][col].append(col - visible[height])
        visible[: height + 1] = [col] * (height + 1)
    visible = [None] * 10
    for col in reversed(range(cols)):
        height = forest[row][col]
        if visible[height] is None:
            scores[row][col].append(cols - col - 1)
        else:
            scores[row][col].append(visible[height] - col)
        visible[: height + 1] = [col] * (height + 1)

for col in range(cols):
    visible = [None] * 10
    for row in range(rows):
        height = forest[row][col]
        if visible[height] is None:
            scores[row][col].append(row)
        else:
            scores[row][col].append(row - visible[height])
        visible[: height + 1] = [row] * (height + 1)
    visible = [None] * 10
    for row in reversed(range(rows)):
        height = forest[row][col]
        if visible[height] is None:
            scores[row][col].append(rows - row - 1)
        else:
            scores[row][col].append(visible[height] - row)
        visible[: height + 1] = [row] * (height + 1)

max_score = max(max(w * e * n * s for w, e, n, s in row) for row in scores)
print(max_score)
