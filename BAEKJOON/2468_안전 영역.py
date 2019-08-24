def bfs(y, x, rain):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = [x, y]
    chk[y][x] = rain
    while queue:
        x = queue.pop(0)
        y = queue.pop(0)
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if 0 <= xi < N and 0 <= yi < N and chk[yi][xi] < rain and board[yi][xi] > rain:
                queue.append(xi)
                queue.append(yi)
                chk[yi][xi] = rain
    return 1

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
chk = [[0] * N for i in range(N)]
max_cnt = 1
for rain in range(1, 101):
    is_fin = True
    cnt = 0
    for j in range(N):
        for i in range(N):
            if board[j][i] > rain and chk[j][i] < rain:
                is_fin = False
                cnt += bfs(j, i, rain)

    if max_cnt < cnt:
        max_cnt = cnt
    if is_fin:
        break

print(max_cnt)
