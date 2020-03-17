def coloring(x1, y1, x2, y2, color):
    global board
    cnt = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] == 0:
                board[i][j] = color
            elif board[i][j] != color and board[i][j] != 3:
                board[i][j] = 3
                cnt += 1
    return cnt

for case in range(1, int(input()) + 1):
    N = int(input())
    count = 0
    board = [[0] * 10 for i in range(10)]
    for i in range(N):
        a1, b1, a2, b2, rb = map(int, input().split())
        count += coloring(a1, b1, a2, b2, rb)
    print(f'#{case} {count}')
