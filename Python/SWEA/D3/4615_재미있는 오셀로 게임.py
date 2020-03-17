from pprint import pprint

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    c = N // 2
    board = [[0] * N for i in range(N)]
    board[c-1][c-1] = 2
    board[c][c] = 2
    board[c-1][c] = 1
    board[c][c-1] = 1

    for m in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        if color == 1:
            another = 2
        else:
            another = 1

        board[y][x] = color        
        for i in range(8):
            xi = x + dx[i]
            yi = y + dy[i]
            if xi < 0 or yi < 0 or xi >= N or yi >= N:
                continue
            if board[yi][xi] == another:
                cnt = 0
                while board[yi][xi] == another:
                    cnt += 1
                    xi += dx[i]
                    yi += dy[i]
                    if xi < 0 or yi < 0 or xi >= N or yi >= N or board[yi][xi] == 0:
                        cnt = 0
                        break
                xi = x + dx[i]
                yi = y + dy[i]

                while cnt != 0:
                    board[yi][xi] = color
                    xi += dx[i]
                    yi += dy[i]
                    cnt -= 1

    black = 0
    white = 0 
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f'#{case} {black} {white}')
