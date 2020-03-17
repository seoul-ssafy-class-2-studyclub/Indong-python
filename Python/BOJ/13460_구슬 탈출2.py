import sys

input = sys.stdin.readline
N, M = map(int, input().split())
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
board = [list(input().rstrip()) for _ in range(N)]
color = [0, 0]
hole = 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            color[0] = (r, c)
        elif board[r][c] == 'B':
            color[1] = (r, c)
        elif board[r][c] == 'O':
            hole = (r, c)

game = [[[[[] for i in range(4)] for j in range(4)] for k in range(2)] for m in range(10)]

red_r, red_c = color[0]
blue_r, blue_c = color[1]
for di in range(4):
    if (di == 0 and red_r < blue_r) or 


print(board)
print(color)
print(hole)

