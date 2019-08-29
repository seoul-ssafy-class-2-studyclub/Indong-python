def calc(idx, w, speed, di):
    idx += speed
    while True:
        if 0 <= idx <= w:
            return idx, di
        if idx > w:
            idx = 2 * w - idx
            if di == 2:
                di = 1
            elif di == 3:
                di = 4
        elif idx < 0:
            idx = abs(idx)
            if di == 1:
                di = 2
            elif di == 4:
                di = 3
        

R, C, M = map(int, input().split())
queue = []
board = [[[] for i in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    board[r][c] = [s, d, z]
    queue.append([r, c])
print(board)
print(queue)
print('------')
fish = 0
for i in range(C):
    
    for j in range(R):
        if board[j][i]:
            print(j, i, board[j][i])
            fish += board[j][i][2]
            board[j][i] = []
            break
    for j in range(len(queue)):
        r, c = queue.pop(0)
        if not board[r][c]:
            continue
        s, d, z = board[r][c]
        board[r][c] = []
        if d == 1:
            r, d = calc(r, R - 1, -s, d)
        elif d == 2:
            r, d = calc(r, R - 1, s, d)
        elif d == 3:
            c, d = calc(c, C - 1, s, d)
        elif d == 4:
            c, d = calc(c, C - 1, -s, d)
        queue.append([r, c])

        if board[r][c]:
            if z < board[r][c][2]:
                continue
        board[r][c] = [s, d, z]
    print(board)
    print('------')     

print(fish)

# 반례
# 2 2 2
# 1 2 1 2 2
# 2 2 1 1 1
