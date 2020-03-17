def dfs(y, x):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        board[y][x] = -1
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if 0 <= xi < 16 and 0 <= yi < 16 and not board[yi][xi]:
                 stack
