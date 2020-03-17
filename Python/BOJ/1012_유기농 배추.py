import sys
from collections import deque

input = sys.stdin.readline
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(r, c):
    global res
    queue = deque()
    queue.append((r, c))
    farm[r][c] = 2
    while queue:
        y, x = queue.popleft()
        for dy, dx in dxy:
            yi = y + dy
            xi = x + dx
            if 0 <= yi < N and 0 <= xi < M and farm[yi][xi] == 1:
                queue.append((yi, xi))
                farm[yi][xi] = 2
    res += 1

for t in range(1, int(input()) + 1):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    for i in range(K):
        c, r = map(int, input().split())
        farm[r][c] = 1

    res = 0
    for r in range(N):
        for c in range(M):
            if farm[r][c] == 1:
                bfs(r, c)

    print(res)
