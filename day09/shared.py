def new_tail(head, tail):
    (head_x, head_y), (tail_x, tail_y) = head, tail
    if max(abs(head_x - tail_x), abs(head_y - tail_y)) <= 1:
        return tail
    elif head_x < tail_x and head_y == tail_y:
        return (tail_x - 1, tail_y)
    elif head_x > tail_x and head_y == tail_y:
        return (tail_x + 1, tail_y)
    elif head_y < tail_y and head_x == tail_x:
        return (tail_x, tail_y - 1)
    elif head_y > tail_y and head_x == tail_x:
        return (tail_x, tail_y + 1)
    elif head_x < tail_x and head_y < tail_y:
        return (tail_x - 1, tail_y - 1)
    elif head_x > tail_x and head_y < tail_y:
        return (tail_x + 1, tail_y - 1)
    elif head_x < tail_x and head_y > tail_y:
        return (tail_x - 1, tail_y + 1)
    elif head_x > tail_x and head_y > tail_y:
        return (tail_x + 1, tail_y + 1)
