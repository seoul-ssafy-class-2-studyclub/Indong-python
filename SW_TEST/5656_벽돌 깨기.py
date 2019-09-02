from collections import deque
from pprint import pprint

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def demolish(x, y, brick):
    q = deque()
    q.append((x, y, brick))
    board[y][x] = 0
    while q:
        x, y, size = q.popleft()
        for i in range(size):
            for a, b in delta:
                xi = x + (a * i)
                yi = y + (b * i)
                if 0 <= xi < W and 0 <= yi < H:
                    bomb = board[yi][xi]
                    if bomb:
                        if bomb > 1:
                            q.append((xi, yi, bomb))
                        board[yi][xi] = 0


def fall(w, h):
    global board
    new_board = [[[0] * w] for _ in range(h)]
    for c in range(w):
        stack = deque()
        for r in range(h):
            brick = board[r][c]
            if brick:
                stack.append(brick)
        idx = h - 1
        while stack:
            new_board[idx][c] = stack.pop()
            idx -= 1

    board, new_board = new_board, board

first = (2, 1, 1)
second = (2, 2, 3)
W = 10
H = 10

board = [list(map(int, input().split())) for _ in range(H)]
demolish(2, 1, 1)
demolish(2, 2, 3)
fall(W, H)
pprint(board)