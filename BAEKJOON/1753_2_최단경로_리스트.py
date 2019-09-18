from sys import stdin, maxsize
from heapq import heappop, heappush

def dijkstra(start):
    queue = []
    heappush(queue, [0, start])
    dis[start] = 0
    while queue:
        cur_dis, cur = heappop(queue)
        if cur_dis > dis[cur]:
            continue
        for nxt, nxt_dis in adj[cur]:
            temp = dis[cur] + nxt_dis
            if dis[nxt] > temp:
                dis[nxt] = temp
                pre[nxt] = cur
                heappush(queue, [temp, nxt])

V, E = map(int, stdin.readline().split())
K = int(stdin.readline())
INF = maxsize
adj = [[] for _ in range(V + 1)]
dis = [INF] * (V + 1)
pre = [-1] * (V + 1)
for i in range(E):
    u, v, w = map(int, stdin.readline().split())
    adj[u].append((v, w))
dijkstra(K)

for i in range(1, V + 1):
    print(dis[i] if dis[i] != INF else 'INF')
