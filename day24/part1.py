from shared import walk, rows, cols

time = walk((-1, 0), (rows - 1, cols - 1), 0) + 1
print(time)
