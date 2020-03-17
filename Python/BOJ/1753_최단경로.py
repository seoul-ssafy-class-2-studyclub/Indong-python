from sys import stdin, maxsize
from collections import defaultdict
from heapq import heappop, heappush

V, E = map(int, stdin.readline().split())
K = int(stdin.readline())
INF = maxsize
adj = [defaultdict(lambda: 11) for _ in range(V + 1)]
dis = [INF] * (V + 1)
for i in range(E):
    u, v, w = map(int, stdin.readline().split())
    if v not in adj[u]:
        adj[u][v] = w
    elif adj[u][v] > w:
        adj[u][v] = w


queue = []
heappush(queue, [0, K])
dis[K] = 0
while queue:
    cur, node = heappop(queue)
    for nxt, value in adj[node].items():
        temp = dis[node] + value
        if dis[nxt] > temp:
            dis[nxt] = temp
            heappush(queue, [temp, nxt])

for i in range(1, V + 1):
    print(dis[i] if dis[i] != INF else 'INF')
