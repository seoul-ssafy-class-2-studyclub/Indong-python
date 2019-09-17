def checkwall(x, y):
    for i in range(x, x+h):
        for j in range(y, y+w):
            if 0 <= i < N and 0 <= j < M:
                if board[i][j] == 1:
                    return 1
                    
def move(x, y, k=0):
    global res
    if x == fr-1 and y == fc-1:
        if res > k:
            res = k
        return
    for dx, dy in idx:
        if 0 <= x+dx < N and 0 <= y+dy < M and 0 <= x+dx+h-1 < N and 0 <= y+dy+w-1 < M:
            if not checkwall(x+dx, y+dy) and not visit[x+dx][y+dy]:
                visit[x+dx][y+dy] = True
                move(x+dx, y+dy, k+1)
                visit[x+dx][y+dy] = False

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
h, w, sr, sc, fr, fc = map(int, input().split())
idx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
res = 100000000
visit[sr-1][sc-1] = True
move(sr-1, sc-1)
if res == 100000000:
    res = -1
print(res)