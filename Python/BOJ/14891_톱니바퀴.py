from collections import deque

def rotate_gear(idx, d):
    if d == 1:
        gears[idx].rotate()
        d = -1
    else:
        gears[idx].rotate(-1)
        d = 1
    return d


def cycle(idx, d):
    dl = dr = rotate_gear(idx, d)
    left = idx - 1
    right = idx
    while magnetic[left] == 1:
        dl = rotate_gear(left, dl)
        left -= 1
    
    while magnetic[right] == 1:
        dr = rotate_gear(right+1, dr)
        right += 1

    for i in range(1, 4):
        if gears[i][2] != gears[i+1][6]:
            magnetic[i] = 1
        else:
            magnetic[i] = 0
    

gears = [[]] + [deque(list(map(int, input()))) for _ in range(4)]
# 3시 방향: 2, 9시 방향: 6
magnetic = [-1] * 6
for i in range(1, 4):
    if gears[i][2] != gears[i+1][6]:
        magnetic[i] = 1
    else:
        magnetic[i] = 0

K = int(input())
score = 0
for _ in range(K):
    gear, turn = map(int, input().split())
    cycle(gear, turn)

for i in range(1, 5):
    if gears[i][0]:
        score += 2 ** (i - 1)

print(score)
