import sys
from collections import deque

def bfs(cur):
    vis[r][c] = num
    queue = deque()
    queue.append((r, c))
    while queue:
        y, x = queue.popleft()
        for dy, dx in dxy:
            yi = y + dy
            xi = x + dx
            if 0 <= yi < N and 0 <= xi < M and pacific[yi][xi] == cur and not vis[yi][xi]:
                queue.append((yi, xi))
                vis[yi][xi] = num


input = sys.stdin.readline
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
pacific = [list(input().strip()) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
islands = []
ocean = []
num = 1
for r in range(N):
    for c in range(M):
        if not vis[r][c]:
            bfs(pacific[r][c])
            if pacific[r][c] == '.':
                ocean.append(num)
            else:
                islands.append(num)
            num += 1

print(ocean)
print(islands)
adj = [set() for _ in range(num)]

for r in range(N - 1):
    for c in range(M - 1):
        cur = vis[r][c]
        for dr, dc in dxy[1:3]:
            ri = r + dr
            ci = c + dc
            nxt = vis[ri][ci]
            if cur != nxt:
                adj[nxt].add(cur)
                adj[cur].add(nxt)

print(adj)
