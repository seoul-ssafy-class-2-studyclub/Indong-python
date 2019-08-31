import sys

def calc(idx_s, w, speed, di):
    while True:
        idx_s += speed
        if 0 <= idx_s <= w:
            return idx_s, di
        if idx_s >= w:
            speed = w - idx_s
            idx_s = w
            if di == 2:
                di = 1
            elif di == 3:
                di = 4
        if idx_s <= 0:
            speed = abs(idx_s)
            idx_s = 0
            if di == 1:
                di = 2
            elif di == 4:
                di = 3
        

R, C, M = map(int, sys.stdin.readline().split())
sharks = []
board = [[0 for i in range(C)] for _ in range(R)]
chk = [[0 for i in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    r, c = r - 1, c - 1
    sharks.append([r, c, s, d, z])
    board[r][c] = sharks[-1]

fish = 0
for i in range(C):
    for j in range(R):
        if board[j][i]:
            fish += board[j][i][4]
            board[j][i][4] = -1
            board[j][i] = 0
            break

    for j in range(len(sharks)):
        r, c, s, d, z = sharks[j]
        if z == -1:
            continue
        board[r][c] = 0

        if d == 1:
            r, d = calc(r, R - 1, -s, d)
        elif d == 2:
            r, d = calc(r, R - 1, s, d)
        elif d == 3:
            c, d = calc(c, C - 1, s, d)
        elif d == 4:
            c, d = calc(c, C - 1, -s, d)
        sharks[j][0] = r
        sharks[j][1] = c
        sharks[j][3] = d

        if not chk[r][c]:
            chk[r][c] = sharks[j]
        else:
            if chk[r][c][4] < sharks[j][4]:
                chk[r][c][4] = -1
                chk[r][c] = sharks[j]
            else:
                sharks[j][4] = -1

    board, chk = chk, board

print(fish)
