from sys import stdin
from collections import deque

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def spread():
    queue = deque(virus[:])
    cnt_virus = 0
    while queue:
        y, x = queue.popleft()
        for a, b in delta:
            xi = x + a
            yi = y + b
            if 0 <= xi < M and 0 <= yi < N and not temp[yi][xi]:
                temp[yi][xi] = 2
                cnt_virus += 1
                queue.append((yi, xi))
    return cnt_virus


N, M = map(int, input().split())

board = [list(map(int, stdin.readline().split())) for _ in range(N)]
cand = []
virus = []
max_cnt = 0
cnt = 0
for j in range(N):
    for i in range(M):
        if board[j][i] == 0:
            cand.append((j, i))
            cnt += 1
        elif board[j][i] == 2:
            virus.append((j, i))

L = len(cand)
for i in range(L):
    for j in range(i + 1, L):
        for k in range(j + 1, L):
            temp = [row[:] for row in board]
            y1, x1 = cand[i]
            y2, x2 = cand[j]
            y3, x3 = cand[k]
            temp[y1][x1], temp[y2][x2], temp[y3][x3] = 1, 1, 1
            safe = cnt - spread() - 3
            if safe > max_cnt:
                max_cnt = safe

print(max_cnt)
