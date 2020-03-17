from heapq import heappush, heappop

INF = float('inf')
def djikstra():
    cost = [INF] * (N + 1)
    cost[0] = 0
    queue = []
    heappush(queue, (0, 0))
    while queue:
        cur_cost, cur = heappop(queue)
        if cur_cost > cost[cur]:
            continue
        for nxt, nxt_cost in adj[cur]:
            temp = cost[cur] + nxt_cost
            if cost[nxt] > temp:
                cost[nxt] = temp
                heappush(queue, (temp, nxt))
    return cost[N]


for case in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for i in range(E):
        f, t, dis = map(int, input().split())
        adj[f].append((t, dis))

    res = djikstra()
    print(f'#{case} {res}')
    