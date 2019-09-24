from sys import stdin
from heapq import heappop, heappush
from itertools import combinations

def calc_dis(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

N, M, D = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(N)]
archers = list(combinations(range(M), 3))
enemies = [(r, c) for c in range(M) for r in range(N) if game[r][c]]
size = len(enemies)
chk = [0] * size

for x, y, z in archers:
    q = [[] for _ in range(3)]

    for idx, (r, c) in enumerate(enemies):
        heappush(q[0], (calc_dis(N, x, r, c), c, r, idx))
        heappush(q[1], (calc_dis(N, y, r, c), c, r, idx))
        heappush(q[2], (calc_dis(N, z, r, c), c, r, idx))

    cnt = 0
    vis = [False] * size
    for i in range(N):
        is_fin = True
        temp = [False] * size 
        for j in range(3):
            if not q[j]:
                continue
            is_fin = False
            hit = False
            for _ in range(len(q[j])):
                dis, c, r, idx = heappop(q[j])
                if vis[idx]:
                    continue
                if dis <= D and not hit:
                    temp[idx] = 1
                    hit = True
                elif r + 1 == N and temp[idx] != 1:
                    temp[idx] = 2
                else:
                    heappush(q[j], (dis - 1, c, r + 1, idx))
        
        if is_fin:
            break

        for j in range(size):
            if temp[j]:
                vis[j] = temp[j]

    for chk in vis:
        if chk == 1:
            cnt += 1
    print(vis)
