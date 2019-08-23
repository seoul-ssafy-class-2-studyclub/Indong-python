import sys

opened_dice = [None, 6, 4, 5, 2, 3, 1]

def stacking(dice, c):
    c_idx = dice.index(c)
    nxt = dice[opened_dice[c_idx]]
    max_num = 0
    for i in dice[1:]:
        if i == c or i == nxt:
            continue
        if max_num < i:
            max_num = i

    return max_num, nxt


dices = []
for game in range(int(sys.stdin.readline())):
    dices.append([None] + list(map(int, sys.stdin.readline().split())))

result = 0
for i in range(1, 7):
    c = dices[0][i]
    max_num = 0
    for j in range(len(dices)):
        temp = stacking(dices[j], c)
        max_num += temp[0]
        c = temp[1]
    if result < max_num:
        result = max_num
print(result)

