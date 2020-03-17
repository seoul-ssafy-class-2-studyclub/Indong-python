import sys
from collections import deque

def bfs(start):
    vis = [False] * (V + 1)
    queue = deque()
    queue.append((start, 0))
    vis[start] = True
    terminal = 0
    res = 0
    while queue:
        node, total = queue.popleft()
        for nxt, dis in adj[node]:
            if not vis[nxt]:
                vis[nxt] = True
                temp = dis + total
                queue.append((nxt, temp))
                if res < temp:
                    res = temp
                    terminal = nxt

    return terminal, res


input = sys.stdin.readline
V = int(input())
adj = [[] for _ in range(V + 1)]
for i in range(V):
    info = list(map(int, input().split()))
    node = info[0]
    for j in range(1, len(info) - 1, 2):
        adj[node].append((info[j], info[j+1]))

temp, dis = bfs(1)
terminal, res = bfs(temp)

print(res)
