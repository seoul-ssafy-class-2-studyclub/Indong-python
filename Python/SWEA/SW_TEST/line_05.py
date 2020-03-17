from sys import stdin
from collections import deque

m, n = map(int, input().split())
x, y = map(int, input().split())

d = [(1, 0), (0, 1)]
if y > n or x > m:
    print('fail')
else:
    board = [[0] * (m + 1) for _ in range(n + 1)]
    queue = deque()
    queue.append((0, 0, 0))
    board[0][0] = 1
    res = 0
    while queue:
        r, c, cnt = queue.popleft()
        for b, a in d:
            ri = r + b
            ci = c + a
            if 0 <= ri < n and 0 <= ci < m:
                if ri == y and ci == x and not res:
                    res = cnt + 1
                elif not board[ri][ci]:
                    queue.append((ri, ci, cnt+1))
                board[ri][ci] += board[r][c]

    print(res)
    print(board[y][x])
        