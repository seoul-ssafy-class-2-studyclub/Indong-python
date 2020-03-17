from collections import deque

dxy =  [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
                
for case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    count = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.':
                board[r][c] = 0
            elif board[r][c] == '*':
                for dr, dc in dxy:
                    ri = r + dr
                    ci = c + dc
                    if 0 <= ri < N and 0 <= ci < N and board[ri][ci] != '*' and board[ri][ci] != 1:
                        board[ri][ci] = 1
                        count += 1

    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                count += 1
                queue = deque()
                queue.append((r, c))
                board[r][c] = -1
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in dxy:
                        yi = y + dy
                        xi = x + dx
                        if 0 <= yi < N and 0 <= xi < N:
                            if board[yi][xi] == 0:
                                queue.append((yi, xi))
                            elif board[yi][xi] == 1:
                                count -= 1
                            board[yi][xi] = -1

    print(f'#{case} {count}')
