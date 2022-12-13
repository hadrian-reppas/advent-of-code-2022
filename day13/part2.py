from functools import cmp_to_key
from shared import less_than

inp = open("input.txt").read()

packets = [[[2]], [[6]]]
for pair in inp.split("\n\n"):
    a, b = pair.split("\n")
    packets.append(eval(a))
    packets.append(eval(b))

cmp = lambda a, b: [1, -1][less_than(a, b)]
packets.sort(key=cmp_to_key(cmp))

index1 = packets.index([[2]]) + 1
index2 = packets.index([[6]]) + 1
print(index1 * index2)
