from shared import get_password, maze


def move(row, col, facing):
    if row == 0 and col in range(50, 100) and facing == 3:
        new = col + 100, 0, 0
    elif row == 0 and col in range(100, 150) and facing == 3:
        new = 199, col - 100, 3
    elif row in range(0, 50) and col == 50 and facing == 2:
        new = 149 - row, 0, 0
    elif row in range(0, 50) and col == 149 and facing == 0:
        new = 149 - row, 99, 2
    elif row == 49 and col in range(100, 150) and facing == 1:
        new = col - 50, 99, 2
    elif row in range(50, 100) and col == 50 and facing == 2:
        new = 100, row - 50, 1
    elif row in range(50, 100) and col == 99 and facing == 0:
        new = 49, row + 50, 3
    elif row == 100 and col in range(50) and facing == 3:
        new = col + 50, 50, 0
    elif row in range(100, 150) and col == 0 and facing == 2:
        new = 149 - row, 50, 0
    elif row in range(100, 150) and col == 99 and facing == 0:
        new = 149 - row, 149, 2
    elif row == 149 and col in range(50, 100) and facing == 1:
        new = col + 100, 49, 2
    elif row in range(150, 200) and col == 0 and facing == 2:
        new = 0, row - 100, 1
    elif row in range(150, 200) and col == 49 and facing == 0:
        new = 149, row - 100, 3
    elif row == 199 and col in range(50) and facing == 1:
        new = 0, col + 100, 1
    elif facing == 0:
        new = row, col + 1, 0
    elif facing == 1:
        new = row + 1, col, 1
    elif facing == 2:
        new = row, col - 1, 2
    else:
        new = row - 1, col, 3
    new_row, new_col, new_facing = new
    if maze[new_row][new_col]:
        return new
    return row, col, facing


print(get_password(move))
