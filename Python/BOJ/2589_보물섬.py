# board = [['W', 'L', 'L', 'W', 'W', 'W', 'L'],
# ['L', 'L', 'L', 'W', 'L', 'L', 'L'],
# ['L', 'W', 'L', 'W', 'L', 'W', 'W'],
# ['L', 'W', 'L', 'W', 'L', 'L', 'L'],
# ['W', 'L', 'L', 'W', 'L', 'W', 'W']]


def bfs(y, x):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    queue = []
    vis[y][x] = True
    queue.append((x, y))
    length = -1
    while queue:
        length += 1
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            for i in range(4):
                xi = x + dx[i]
                yi = y + dy[i]
                if 0 <= xi < M and 0 <= yi < N and board[yi][xi] == 'L' and not vis[yi][xi]:
                    vis[yi][xi] = True
                    queue.append((xi, yi))

    return length


N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(input()))

result = 0
for j in range(N):
    for i in range(M):
        if board[j][i] == 'L':
            vis = [[False] * M for i in range(N)]
            cnt = bfs(j, i)
            if result < cnt:
                result = cnt

print(result)
