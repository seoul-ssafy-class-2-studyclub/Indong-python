from sys import stdin, maxsize
from heapq import heappop, heappush

input = stdin.readline
INF = maxsize

def djikstra(start, end):
    cost[start] = 0
    queue = []
    heappush(queue, (0, start))

    while queue:
        cur_cost, cur = heappop(queue)
        if cur_cost > cost[cur]:
            continue
        for nxt, nxt_cost in adj[cur]:
            temp = cost[cur] + nxt_cost
            if temp < cost[nxt]:
                cost[nxt] = temp
                heappush(queue, (temp, nxt))
    
    return cost[end]


N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
cost = [INF] * (N + 1)
for i in range(M):
    f, t, c = map(int, input().split())
    adj[f].append((t, c))
start, end = map(int, input().split())

res = djikstra(start, end)
print(res)