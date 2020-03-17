def dfs(y, x):
    global board

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    stack = [(x, y)]
    while stack:
        board[y][x] = -1
        x, y = stack.pop()
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if 0 <= xi < N and 0 <= yi < N:
                if board[yi][xi] == 3:
                    return 1
                if board[yi][xi] == 0:
                    stack.append((xi, yi))
    return 0


for case in range(1, int(input()) + 1):
    N = int(input())
    board = []
    for row in range(N):
        board.append(list(map(int, input())))
    
    result = 0
    for j in range(N):
        for i in range(N):
            if board[j][i] == 2:
                result = dfs(j, i)
                break
                
    print(f'#{case} {result}')
