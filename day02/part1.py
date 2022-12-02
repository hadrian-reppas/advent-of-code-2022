inp = open("input.txt").read()

win = {(2, 1), (3, 2), (1, 3)}

score = 0
for line in inp.split("\n"):
    me = ord(line[2]) - ord("W")
    them = ord(line[0]) - ord("@")
    if (me, them) in win:
        score += 6 + me
    elif me == them:
        score += 3 + me
    else:
        score += me

print(score)
