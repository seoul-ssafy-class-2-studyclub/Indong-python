import sys

input = sys.stdin.readline
dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# gen = [[] for _ in range(11)]
# gen[0].append(0)
# gen[1].append(1)
# for i in range(2, 11):
#     for j in range(0, i - 1):
#         gen[i].extend(list(map(lambda x: (x + 2) % 4, gen[j])))
#     gen[i].extend(gen[i-1])

N = int(input())
board = [[False] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[y][x] = True
    dc = [d]
    for i in range(g + 1):
        for path in dc[int(2 ** (i-1)):]:
            dy, dx = dxy[path]
            y += dy
            x += dx
            board[y][x] = True
        dc += [(j + 1) % 4 for j in dc[::-1]]

res = 0
for r in range(100):
    for c in range(100):
        if board[r][c] and board[r+1][c] and board[r][c+1] and board[r+1][c+1]:
            res += 1

print(res)
