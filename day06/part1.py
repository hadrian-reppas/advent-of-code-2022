data = open("input.txt").read()

for i in range(len(data)):
    slice = data[i:i + 4]
    if len(set(slice)) == 4:
        break

print(i + 4)
