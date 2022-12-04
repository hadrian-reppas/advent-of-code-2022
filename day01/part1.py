inp = open("input.txt").read()

max_cals = 0
for elf in inp.split("\n\n"):
    cals = sum(int(line) for line in elf.split("\n"))
    max_cals = max(max_cals, cals)

print(max_cals)
