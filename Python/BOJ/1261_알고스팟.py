from heapq import heappop, heappush

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INF = float('inf')
M, N = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
chk = [[INF] * M for _ in range(N)]

queue = []
heappush(queue, (0, 0, 0))
chk[0][0] = 0
while queue:
    cur, y, x = heappop(queue)
    if cur > chk[y][x]:
        continue
    for b, a in dxy:
        yi = y + b
        xi = x + a
        if 0 <= yi < N and 0 <= xi < M:
            nxt = chk[y][x] + board[yi][xi]
            if chk[yi][xi] > nxt:
                chk[yi][xi] = nxt
                heappush(queue, (nxt, yi, xi))

print(chk[N-1][M-1])
