move = [[3, 2], [2, 3], [1, 0], [0, 1]]

for case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    x, y = 0, 0
    di = 3
    while True:
        if di == 0:
            y -= 1
        elif di == 1:
            y += 1
        elif di == 2:
            x -= 1
        else:
            x += 1
        if 0 > x or x >= N or 0 > y or y >= N:
            break
        if board[y][x]:
            di = move[di][board[y][x] - 1]
        cnt += 1
    print('#{0} {1}'.format(case, cnt))
