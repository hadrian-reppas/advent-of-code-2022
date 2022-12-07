inp = open("input.txt").read()

sizes = []
stack = []
for line in inp.split("\n"):
    if line == "$ cd ..":
        size = stack.pop()
        sizes.append(size)
        stack[-1] += size
    elif line.startswith("$ cd "):
        stack.append(0)
    elif line[0].isdigit():
        size, _ = line.split()
        stack[-1] += int(size)

while len(stack) > 1:
    size = stack.pop()
    sizes.append(size)
    stack[-1] += size

sizes.append(stack.pop())

if __name__ == "__main__":
    total = 0
    for size in sizes:
        if size <= 100000:
            total += size

    print(total)
