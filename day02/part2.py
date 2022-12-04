inp = open("input.txt").read()

win = {(2, 1), (3, 2), (1, 3)}

move = {
    (1, 1): 3, (1, 2): 1, (1, 3): 2,
    (2, 1): 1, (2, 2): 2, (2, 3): 3,
    (3, 1): 2, (3, 2): 3, (3, 3): 1,
}

score = 0
for line in inp.split("\n"):
    them = ord(line[0]) - ord("A") + 1
    outcome = ord(line[2]) - ord("X") + 1
    me = move[(them, outcome)]
    if (me, them) in win:
        score += 6 + me
    elif me == them:
        score += 3 + me
    else:
        score += me

print(score)
