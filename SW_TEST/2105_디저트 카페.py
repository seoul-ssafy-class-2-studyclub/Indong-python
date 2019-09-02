delta = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
 
 
def dfs(y, x, vis, di=0, cnt=0):
    global max_cnt
    global start
    vis = vis[:]
    vis[board[y][x]] = True
    cnt += 1
    if di == 2:
        if x + y == start[0] + start[1]:
            di = [3]
        else:
            di = [2]
    elif di == 3:
        di = [3]
    else:
        di = [di, di + 1]
 
    for d in di:
        xi = x + delta[d][0]
        yi = y + delta[d][1]
        if (yi, xi) == start:
            if max_cnt < cnt:
                max_cnt = cnt
            return True
        if 0 <= xi < N and 0 <= yi < N and not vis[board[yi][xi]]:
            dfs(yi, xi, vis, d, cnt)
 
 
for case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    chk = [[0] * N for _ in range(N)]
    max_cnt = -1
     
    for i in range(N - 1):
        for j in range(1, N - 1):
            vis = [False] * 101
            start = i, j
            dfs(i, j, vis)
     
    print(f'#{case} {max_cnt}')
    