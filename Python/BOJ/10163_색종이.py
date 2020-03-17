board = [[0] * 101 for i in range(101)]

N = int(input())
result = [0] * (N + 1)
for i in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    y = 100 - y
    for j in range(w):
        for k in range(h):
            board[y-k][x+j] = i

for i in range(101):
    for j in range(101):
        if board[i][j] == 0:
            continue
        result[board[i][j]] += 1

for i in result[1:]:
    print(i)
    