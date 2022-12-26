from shared import walk, rows, cols

time1 = walk((-1, 0), (rows - 1, cols - 1), 0) + 1
time2 = walk((rows, cols - 1), (0, 0), time1) + 1
time3 = walk((-1, 0), (rows - 1, cols - 1), time2) + 1

print(time3)
