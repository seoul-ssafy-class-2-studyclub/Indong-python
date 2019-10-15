import sys
from collections import deque
sys.setrecursionlimit(10**7)

def dfs(y, x, cur):
    vis[y][x] = num
    for dy, dx in dxy:
        yi = y + dy
        xi = x + dx
        if 0 <= yi < N and 0 <= xi < M:
            nxt = vis[yi][xi]
            if pacific[yi][xi] == cur and not nxt:
                dfs(yi, xi, cur)
            elif pacific[yi][xi] != cur and nxt:
                if con[nxt] == num:
                    continue
                adj[num].append(nxt)
                adj[nxt].append(num)
                con[num] = num
                con[nxt] = num


def init():
    for i in range(num):
        con[i] = 0
    for r in range(N):
        for c in range(M):
            if pacific[r][c] == '#':
                is_sum[vis[r][c]] = 1


def go(now):
    global order
    ret = num - 1
    discovered[now] = order
    order += 1
    stack.append(now)
    for nxt in adj[now]:
        if not discovered[nxt]:
            go(nxt)
            if is_sum[now] and discovered[nxt] == discovered[now]:
                while stack and stack[-1] != now:
                    con[stack.pop()] = 1
            stack.append(now)
        ret = min(ret, discovered[nxt])
    discovered[now] = ret
    return


input = sys.stdin.readline
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
pacific = [list(input().strip()) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
adj = [[]]
con = [0] * 4000001
num = 1
for r in range(N):
    for c in range(M):
        if not vis[r][c]:
            adj.append([])
            dfs(r, c, pacific[r][c])
            num += 1

is_sum = [0] * num
discovered = [False] * num
stack = deque()
order = 1

init()
go(1)

for r in range(N):
    for c in range(M):
        if pacific[r][c] == '.':
            continue
        num = vis[r][c]
        if con[num] and discovered[num] != 1:
            pacific[r][c] = 'X'
        else:
            pacific[r][c] = 'O'


for r in range(N):
    print(''.join(pacific[r]))
