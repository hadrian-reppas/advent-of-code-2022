data = open("input.txt").read()

for i in range(len(data)):
    slice = data[i:i + 14]
    if len(set(slice)) == 14:
        break

print(i + 14)
