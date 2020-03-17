import sys

d = [(-1,0),(0,1),(1,0),(0,-1)]
def spread():
    chk = [[0] * C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if board[y][x] >= 5:
                dust = board[y][x]
                s_dust = dust // 5
                for a, b in d:
                    xi = x + a
                    yi = y + b
                    if 0 <= xi < C and 0 <= yi < R and board[yi][xi] != -1:
                        chk[yi][xi] += s_dust
                        board[y][x] -= s_dust
            
    for i in range(R):
        for j in range(C):
            board[i][j] += chk[i][j]


def air_cleaner():
    for i in range(air1 - 1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(air2 + 1, R - 1):
        board[i][0] = board[i+1][0]

    for i in range(0, C - 1):
        board[0][i] = board[0][i+1]
        board[R-1][i] = board[R-1][i+1]

    for i in range(air1):
        board[i][C-1] = board[i+1][C-1]
    for i in range(R - 1, air2, -1):
        board[i][C-1] = board[i-1][C-1]

    for i in range(C - 1, 1, -1):
        board[air1][i] = board[air1][i-1]
        board[air2][i] = board[air2][i-1]

    board[air1][1] = 0
    board[air2][1] = 0
    


R, C, T = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for d in range(R)]
air1, air2 = 0, 0
for i in range(R):
    if board[i][0] == -1:
        air1 = i
        air2 = i + 1
        break

for _ in range(T):
    spread()
    air_cleaner()

result = 0
for i in range(R):
    result += sum(board[i])
print(result + 2)
