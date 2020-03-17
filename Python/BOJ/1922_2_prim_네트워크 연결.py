import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = float('inf')

def prim(start):
    cost = [INF] * (N + 1)
    vis = [False] * (N + 1)
    q = []
    heappush(q, (0, start))
    cost[start] = 0
    while q:
        cur_cost, node = heappop(q)
        vis[node] = True
        for child, nxt_cost in adj[node]:
            if cost[child] > nxt_cost and not vis[child]:
                cost[child] = nxt_cost
                heappush(q, (nxt_cost, child))
    return sum(cost[1:])


N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
for i in range(M):
    n1, n2, w = map(int, input().split())
    adj[n1].append((n2, w))
    adj[n2].append((n1, w))

print(prim(1))
