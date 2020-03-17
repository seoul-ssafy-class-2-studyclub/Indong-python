from sys import stdin, maxsize
from heapq import heappop, heappush
input = stdin.readline
INF = maxsize

def djikstra(start, adj):
    dis = [INF] * (N + 1)
    dis[start] = 0
    queue = []
    heappush(queue, (0, start))
    while queue:
        cur_cost, cur = heappop(queue)
        if cur_cost > dis[cur]:
            continue
        for nxt, nxt_cost in adj[cur]:
            temp = dis[cur] + nxt_cost
            if dis[nxt] > temp:
                dis[nxt] = temp
                heappush(queue, (temp, nxt))

    return dis
                

N, M, X = map(int, input().split())
adj = [[] for _ in range(N + 1)]
rev_adj = [[] for _ in range(N + 1)]
for i in range(M):
    f, t, time = map(int, input().split())
    adj[f].append((t, time))
    rev_adj[t].append((f, time))

dis = djikstra(X, adj)
rev_dis = djikstra(X, rev_adj)

res = 0
for i in range(1, N + 1):
    cost = dis[i] + rev_dis[i]
    if cost > res:
        res = cost

print(res)
