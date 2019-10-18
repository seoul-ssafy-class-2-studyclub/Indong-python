import sys
from itertools import permutations

def hit(h):
    global score
    for i in range(2, -1, -1):
        if base[i]:
            base[i] = 0
            nxt = i + h
            if nxt >= 3:
                score += 1
            else:
                base[nxt] = 1
    if h == 4:
        score += 1
    else:
        base[h-1] = 1


input = sys.stdin.readline
N = int(input())
inning = [list(map(int, input().split())) for _ in range(N)]
max_score = 0
for hitter in list(permutations(range(1, 9), 8)):
    order = 0
    score = 0
    hitter = list(hitter[:3]) + [0] + list(hitter[3:])
    for i in range(N):
        base = [0, 0, 0]
        outcnt = 0
        while outcnt < 3:
            now = hitter[order]
            if inning[i][now]:
                hit(inning[i][now])
            else:
                outcnt += 1
            order += 1
            if order == 9:
                order = 0

    if score > max_score:
        max_score = score

print(max_score)
