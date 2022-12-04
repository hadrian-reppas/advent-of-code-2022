inp = open("input.txt").read()

count = 0
for line in inp.split("\n"):
    left, right = line.split(",")
    left_low, left_high = map(int, left.split("-"))
    right_low, right_high = map(int, right.split("-"))
    if (
        left_low in range(right_low, right_high + 1)
        or left_high in range(right_low, right_high + 1)
        or right_low in range(left_low, left_high + 1)
        or right_high in range(left_low, left_high + 1)
    ):
        count += 1

print(count)
