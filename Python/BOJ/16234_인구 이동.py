from sys import stdin
from collections import deque


def open(r, c):
    global flag
    queue = deque()
    idx = deque()
    cont = land[r][c]
    queue.append((r, c))
    idx.append((r, c))
    vis[r][c] += 1
    while queue:
        y, x = queue.popleft()
        now = land[y][x]
        for b, a in delta:
            yi = y + b
            xi = x + a
            if 0 <= yi < N and 0 <= xi < N and vis[yi][xi] < ans:
                nxt = land[yi][xi]
                if L <= abs(now - nxt) <= R:
                    queue.append((yi, xi))
                    idx.append((yi, xi))
                    cont += nxt
                    vis[yi][xi] += 1
    if len(idx) == 1:
        return False
    
    flag = True
    avg = cont // len(idx)
    while idx:
        y, x = idx.popleft()
        land[y][x] = avg


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, L, R = map(int, stdin.readline().split())
land = [list(map(int, stdin.readline().split())) for _ in range(N)]
vis = [[-1] * N for _ in range(N)]
cnt = -1
ans = 0
flag = True

while flag:
    flag = False
    cnt += 1
    for r in range(N):
        for c in range(N):
            if vis[r][c] < ans:
                open(r, c)
    if flag:
        ans += 1

print(cnt)
