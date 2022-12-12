from collections import deque
from shared import grid, end, rows, cols, can_move

queue = deque([(*end, 0)])
seen = set()
while True:
    row, col, dist = queue.popleft()

    if grid[row][col] == "a":
        break
    elif (row, col) in seen:
        continue
    seen.add((row, col))

    if row > 0 and can_move(grid[row - 1][col], grid[row][col]):
        queue.append((row - 1, col, dist + 1))
    if col > 0 and can_move(grid[row][col - 1], grid[row][col]):
        queue.append((row, col - 1, dist + 1))
    if row < rows - 1 and can_move(grid[row + 1][col], grid[row][col]):
        queue.append((row + 1, col, dist + 1))
    if col < cols - 1 and can_move(grid[row][col + 1], grid[row][col]):
        queue.append((row, col + 1, dist + 1))

print(dist)
