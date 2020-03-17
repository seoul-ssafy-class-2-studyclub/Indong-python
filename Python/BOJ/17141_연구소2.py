from collections import deque
from sys import stdin

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def spread(queue, safe, cnt=-1):
    while queue:
        cnt += 1
        if min_time != -1 and cnt > min_time:
            return cnt, safe
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for a, b in delta:
                xi = x + a
                yi = y + b
                if 0 <= xi < N and 0 <= yi < N and lab[yi][xi] != 1:
                    lab[yi][xi] = 1
                    safe -= 1
                    queue.append((yi, xi))
    return cnt, safe


def comb(arr=[], k=-1, cnt=0):
    if cnt == M:
        virus.append(arr)
        return True
    for i in range(k + 1, cand):
        comb(arr+[idx[i]], i, cnt+1)
    

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
idx = []
safe = N * N - M
for j in range(N):
    for i in range(N):
        if board[j][i] == 2:
            idx.append((j, i))
        elif board[j][i] == 1:
            safe -= 1
cand = len(idx)
virus = []
comb()

min_time = -1
for queue in virus:
    lab = [row[:] for row in board]
    queue = deque(queue)
    for y, x in queue:
        lab[y][x] = 1
    time, chk = spread(queue, safe)
    if chk:
        continue
    if min_time == -1 or min_time > time:
        min_time = time

print(min_time)
