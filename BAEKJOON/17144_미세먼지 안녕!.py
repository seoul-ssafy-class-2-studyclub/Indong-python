from copy import deepcopy

def spread(y, x, dust):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    s_dust = dust // 5
    for i in range(4):
        xi = x + dx[i]
        yi = y + dy[i]
        if 0 <= xi < C and 0 <= yi < R and chk[yi][xi] != -1:
            chk[yi][xi] += s_dust
            dust -= s_dust
            queue.append((xi, yi))
    print(dust)
    chk[y][x] += dust


R, C, T = map(int, input().split())
queue = []
board = [list(map(int, input().split())) for d in range(R)]
chk = [[0] * C for _ in range(R)]
air_cleaner = []
print(board)
for i in range(R):
    for j in range(C):
        if board[i][j]:
            if board[i][j] != -1:
                queue.append((j, i))
            else:
                air_cleaner.append(i)
                chk[i][j] = -1

for i in range(len(queue)):
    x, y = queue.pop(0)
    if board[y][x]:
        dust = board[y][x]
        board[y][x] = 0
        spread(y, x, dust)

for i in range(1, air_cleaner[0], -1):
    chk[i][0] = chk[i-1][0]
chk[0][:C-1] = chk[0][1:C]

board, chk = chk, board
