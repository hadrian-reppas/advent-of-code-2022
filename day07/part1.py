sizes, stack = [], []
for line in open("input.txt"):
    if line.startswith("$ cd .."):
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
    total = sum(filter(lambda size: size <= 100000, sizes))
    print(total)
