inp = open("input.txt").read()

count = 0
for line in inp.split("\n"):
    left, right = line.split(",")
    left_low, left_high = map(int, left.split("-"))
    right_low, right_high = map(int, right.split("-"))
    if (left_low <= right_low and right_high <= left_high) or (
        right_low <= left_low and left_high <= right_high
    ):
        count += 1

print(count)
