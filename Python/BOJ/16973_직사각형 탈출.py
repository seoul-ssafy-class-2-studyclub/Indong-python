from collections import deque
from sys import stdin
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, stdin.readline().split())
Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1
walls = []
res = -1
for r in range(N):
    for c in range(M):
        if board[r][c]:
            walls.append((r, c))

queue = deque([(Sr, Sc, 0)])
board[Sr][Sc] = -1
while queue:
    y, x, cnt = queue.popleft()
    if y == Fr and x == Fc:
        res = cnt
        break

    for b, a in dxy:
        yi = y + b
        xi = x + a
        if 0 <= yi and yi + H - 1 < N and 0 <= xi and xi + W - 1 < M and not board[yi][xi]:
            flag = True
            for wy, wx in walls:
                if yi <= wy < yi + H and xi <= wx < xi + W:
                    flag = False
                    break
            if flag:
                queue.append((yi, xi, cnt+1))
            board[yi][xi] = -1

print(res)
