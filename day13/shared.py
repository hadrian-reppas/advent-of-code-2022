def less_than(a, b):
    a, b = list(reversed(a)), list(reversed(b))
    while a and b:
        x, y = a.pop(), b.pop()
        if isinstance(x, int) and isinstance(y, int):
            o = True if x < y else False if y < x else None
        elif isinstance(x, list) and isinstance(y, list):
            o = less_than(x, y)
        elif isinstance(x, int) and isinstance(y, list):
            o = less_than([x], y)
        else:
            o = less_than(x, [y])

        if o is not None:
            return o

    if b:
        return True
    elif a:
        return False
