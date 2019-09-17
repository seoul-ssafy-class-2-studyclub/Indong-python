import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)

def dfs(node):
    vis[node] = True
    for nxt in adj[node]:
        if not vis[nxt]:
            dfs(nxt)

V, E = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(V + 1)]
vis = [False] * (V + 1)
for i in range(E):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

res = 0
for i in range(1, V + 1):
    if vis[i]:
        continue
    res += 1
    dfs(i)

print(res)
