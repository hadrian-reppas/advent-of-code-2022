lines = open("input.txt").read().split("\n")

snafu_digits = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}
digits = "012=-"


def snafu_to_int(snafu):
    i = 0
    for n, c in enumerate(reversed(snafu)):
        i += 5**n * snafu_digits[c]
    return i


def int_to_snafu(i):
    snafu = ""
    while i:
        snafu = digits[i % 5] + snafu
        i = i // 5 + (i % 5 > 2)
    return snafu


total = sum(snafu_to_int(line) for line in lines)
print(int_to_snafu(total))
