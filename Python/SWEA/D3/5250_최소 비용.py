from heapq import heappop, heappush

def dijkstra():
    cost = [[INF] * N for _ in range(N)]
    cost[0][0] = 0
    queue = []
    heappush(queue, (0, 0, 0))
    while queue:
        cur, y, x = heappop(queue)
        if cur > cost[y][x]:
            continue
        for dy, dx in dxy:
            yi = y + dy
            xi = x + dx
            if 0 <= yi < N and 0 <= xi < N:
                temp = board[yi][xi] - board[y][x]
                if temp > 0:
                    nxt = cur + temp + 1
                else:
                    nxt = cur + 1
                if cost[yi][xi] > nxt:
                    cost[yi][xi] = nxt
                    heappush(queue, (nxt, yi, xi))
    return cost[N-1][N-1]


INF = float('inf')
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    res = dijkstra()
    print(f'#{case} {res}')
