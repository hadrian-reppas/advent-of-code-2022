from collections import deque
from shared import grid, start, end, rows, cols, can_move

queue = deque([(*start, 0)])
seen = set()
while True:
    row, col, dist = queue.popleft()

    if (row, col) == end:
        break
    elif (row, col) in seen:
        continue
    seen.add((row, col))

    if row > 0 and can_move(grid[row][col], grid[row - 1][col]):
        queue.append((row - 1, col, dist + 1))
    if col > 0 and can_move(grid[row][col], grid[row][col - 1]):
        queue.append((row, col - 1, dist + 1))
    if row < rows - 1 and can_move(grid[row][col], grid[row + 1][col]):
        queue.append((row + 1, col, dist + 1))
    if col < cols - 1 and can_move(grid[row][col], grid[row][col + 1]):
        queue.append((row, col + 1, dist + 1))

print(dist)
