inp = open("input.txt").read()

calories = []
for elf in inp.split("\n\n"):
    cals = sum(int(line) for line in elf.split("\n"))
    calories.append(cals)

top_three = sorted(calories)[-3:]
print(sum(top_three))
