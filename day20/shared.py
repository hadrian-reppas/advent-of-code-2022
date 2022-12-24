def decrypt(key, n):
    values = [key * int(line) for line in open("input.txt").read().split("\n")]
    array = list(range(len(values)))

    for i in array * n:
        index = array.index(i)
        del array[index]
        move_to = (index + values[i]) % len(array)
        if move_to:
            array.insert(move_to, i)
        else:
            array.append(i)

    start = array.index(values.index(0))
    value1 = values[array[(start + 1000) % len(values)]]
    value2 = values[array[(start + 2000) % len(values)]]
    value3 = values[array[(start + 3000) % len(values)]]
    return value1 + value2 + value3
