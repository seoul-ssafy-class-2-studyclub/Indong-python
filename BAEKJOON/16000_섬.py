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

is_island = [False] * num
for i in islands:
    is_island[i] = True

# print(ocean)
# print(islands)
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

tree = [[] for _ in range(num)]
discovered = [False] * num
is_cut = [False] * num
order = 1
def dfs_tree(node=1):
    global order
    discovered[node] = order
    order += 1
    ret = discovered[node]
    child = 0
    for i in adj[node]:
        nxt = discovered[i]
        if nxt:
            ret = min(ret, nxt)
            continue
        tree[node].append(i)
        child += 1
        prev = dfs_tree(i)
    
        if prev >= discovered[node]:
            is_cut[node] = True

        ret = min(ret, prev)
    
    return ret


dfs_tree()
safe = [True] * num
visited = [False] * num
def chk_unsafe(start):
    stack = deque()
    stack.append(start)
    while stack:
        node = stack.pop()
        visited[node] = True
        for child in tree[node]:
            safe[child] = False
            stack.append(child)


for i in range(num):
    if visited[i]:
        continue
    visited[i] = True
    if is_island[i] and is_cut[i]:
        chk_unsafe(i)
    
for r in range(N):
    for c in range(M):
        if pacific[r][c] == '.':
            continue
        cur = vis[r][c]
        if safe[cur]:
            pacific[r][c] = 'O'
        else:
            pacific[r][c] = 'X'
            
    print(''.join(pacific[r]))

    
# print(is_island)
# print(is_cut)
# print(discovered)
# print(tree)
# print(adj)
# print(safe)
