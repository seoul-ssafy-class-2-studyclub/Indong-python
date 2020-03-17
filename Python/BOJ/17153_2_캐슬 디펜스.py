from itertools import combinations
from sys import stdin

input = stdin.readline

def calc_dis(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


N, M, D = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(N)]

idx_enemies = [[r, c, False] for c in range(M) for r in range(N) if game[r][c]]
size = len(idx_enemies)
res = 0

for archers in combinations(range(M), 3):
    enemies = [row[:] for row in idx_enemies]
    cnt = 0
    for i in range(N):
        targets = [[99, 99, -1], [99, 99, -1], [99, 99, -1]]
        for idx in range(size):
            r, c, dead = enemies[idx]
            if dead:
                continue

            for ah in range(3):
                dis = calc_dis(N, archers[ah], r, c)
                if dis <= D:
                    if dis < targets[ah][0] or (dis == targets[ah][0] and c < targets[ah][1]):
                        targets[ah][0] = dis
                        targets[ah][1] = c
                        targets[ah][2] = idx
                
            if r + 1 == N:
                enemies[idx][2] = True
            else:
                enemies[idx][0] += 1

        chk = []
        for ah in range(3):
            tg_idx = targets[ah][2] 
            if tg_idx != -1 and tg_idx not in chk:
                enemies[tg_idx][2] = True
                chk.append(tg_idx)
                cnt += 1

    if cnt > res:
        res = cnt
    
    if cnt == size:
        break

print(res)
            