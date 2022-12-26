from collections import deque

_, *lines, _ = open("input.txt").read().split("\n")
snow = [line[1:-1] for line in lines]
rows, cols = len(snow), len(snow[0])

vblizzards = [[] for _ in range(cols)]
hblizzards = [[] for _ in range(rows)]

for row, line in enumerate(snow):
    for col, c in enumerate(line):
        if c == ">":
            hblizzards[row].append((col, 1))
        elif c == "<":
            hblizzards[row].append((col, -1))
        elif c == "v":
            vblizzards[col].append((row, 1))
        elif c == "^":
            vblizzards[col].append((row, -1))


def blizzard_at(row, col, time):
    for start_col, v in hblizzards[row]:
        if (start_col + time * v) % cols == col:
            return True
    for start_row, v in vblizzards[col]:
        if (start_row + time * v) % rows == row:
            return True
    return False


def walk(start, end, time):
    queue = deque([(*start, time)])
    seen = set()
    while True:
        row, col, time = queue.popleft()
        if (row, col, time) in seen:
            continue
        seen.add((row, col, time))
        if (row, col) == end:
            return time
        if row > 0 and not blizzard_at(row - 1, col, time + 1):
            queue.append((row - 1, col, time + 1))
        if col > 0 and row < rows and not blizzard_at(row, col - 1, time + 1):
            queue.append((row, col - 1, time + 1))
        if row < rows - 1 and not blizzard_at(row + 1, col, time + 1):
            queue.append((row + 1, col, time + 1))
        if col < cols - 1 and row >= 0 and not blizzard_at(row, col + 1, time + 1):
            queue.append((row, col + 1, time + 1))
        if row not in range(rows) or not blizzard_at(row, col, time + 1):
            queue.append((row, col, time + 1))
