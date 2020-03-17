from sys import stdin
from itertools import combinations as cb
from collections import deque

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def spread(queue, safe, cnt=-1):
    while queue:
        cnt += 1
        if safe == 0:
            break
        if min_time != -1 and cnt > min_time:
            return cnt, safe
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for a, b in delta:
                xi = x + a
                yi = y + b
                if 0 <= xi < N and 0 <= yi < N and lab[yi][xi] != 1:
                    if lab[yi][xi] == 0:
                        safe -= 1
                    lab[yi][xi] = 1
                    queue.append((yi, xi))
    return cnt, safe


N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
idx = []
safe = 0
for j in range(N):
    for i in range(N):
        if board[j][i] == 2:
            idx.append((j, i))
        elif board[j][i] == 0:
            safe += 1

min_time = -1
for queue in cb(idx, M):
    lab = [row[:] for row in board]
    virus = deque(queue)
    for y, x in virus:
        lab[y][x] = 1
    time, chk = spread(virus, safe)
    if chk:
        continue
    if min_time == -1 or min_time > time:
        min_time = time

print(min_time)
