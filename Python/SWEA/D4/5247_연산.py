from heapq import heappop, heappush
from collections import deque

INF = float('inf')

def djikstra(N, M):
    end = M + 201
    if end > 10 ** 6:
        end = 10 ** 6 + 1
    dis = [INF] * end
    dis[N] = 0
    queue = deque([(0, N)])
    while queue:
        cur_cost, cur = queue.popleft()
        if cur_cost > dis[cur]:
            continue
        for i in range(4):
            nxt = -1
            if i == 0 and cur + 1 < end:
                nxt = cur + 1
            elif i == 1 and cur - 1 >= 0:
                nxt = cur - 1
            elif i == 2 and cur * 2 < end:
                nxt = cur * 2
            elif i == 3 and cur - 10 >= 0:
                nxt = cur - 10
            if nxt == -1:
                continue
            temp = dis[cur] + 1
            if dis[nxt] > temp:
                dis[nxt] = temp
                queue.append((temp, nxt))
    return dis[M]


for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    res = djikstra(N, M)
    print(f'#{case} {res}')
