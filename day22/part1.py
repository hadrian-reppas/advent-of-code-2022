from shared import get_password, maze

move_map = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def move(row, col, facing):
    drow, dcol = move_map[facing]
    new_row, new_col = (row + drow) % 200, (col + dcol) % 150
    while maze[new_row][new_col] is None:
        new_row, new_col = (new_row + drow) % 200, (new_col + dcol) % 150
    if maze[new_row][new_col] is True:
        return new_row, new_col, facing
    return row, col, facing


print(get_password(move))
