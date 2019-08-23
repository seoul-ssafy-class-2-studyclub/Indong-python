import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def air(queue):
    queue = queue[:]
    board[0][0] = -1
    while queue:
        x = queue.pop(0)
        y = queue.pop(0)
        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]
            if 0 <= xi < N and 0 <= yi < M:
                if not board[yi][xi]:
                    board[yi][xi] = -1 
                    queue.append(xi)
                    queue.append(yi)
                elif board[yi][xi] == 1:
                    board[yi][xi] = 2
    return queue

board = []
M, N = map(int, sys.stdin.readline().split())
for row in range(M):
    board.append(list(map(int, sys.stdin.readline().split())))

time, cheeze = 0, 0
queue = [0, 0]
while True:
    is_fin = True
    cnt = 0
    queue = air(queue)
    for i in range(M):
        for j in range(N):
            if board[i][j] == 2:
                board[i][j] = 0
                cnt += 1
                queue.append(j)
                queue.append(i)
            elif board[i][j] == 1:
                is_fin = False
    time += 1
    cheeze = cnt
    if is_fin:
        break
    
print(time)
print(cheeze)
            