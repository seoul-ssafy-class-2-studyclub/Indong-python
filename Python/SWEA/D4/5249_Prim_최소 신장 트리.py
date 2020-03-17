from heapq import heappush, heappop

INF = float('inf')
for case in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    cost = [INF] * (V + 1)
    vis = [False] * (V + 1)
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append((n2, w))
        adj[n2].append((n1, w))

    cost[0] = 0
    queue = []
    heappush(queue, (0, 0))
    while queue:
        cur, node = heappop(queue)
        vis[node] = True
        for child, nxt in adj[node]:
            if vis[child]:
                continue
            if cost[child] > nxt:
                cost[child] = nxt
                heappush(queue, (nxt, child))

    print(f'#{case} {sum(cost)}')
