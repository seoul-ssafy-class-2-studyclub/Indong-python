dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result_list = []

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input())))

for j in range(N):
    for i in range(N):
        if board[j][i] == 1:
            cnt = 1
            board[j][i] = -1
            queue = [(i, j)]
            while queue:
                x, y = queue.pop(0)
                for k in range(4):
                    xk = x + dx[k]
                    yk = y + dy[k]
                    if 0 <= xk < N and 0 <= yk < N and board[yk][xk] == 1:
                        queue.append((xk, yk))
                        board[yk][xk] = -1
                        cnt += 1
            result_list += [cnt]

result_list.sort()
print(len(result_list))
for i in range(len(result_list)):
    print(result_list[i])
