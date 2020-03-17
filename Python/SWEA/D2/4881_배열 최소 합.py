def btk(vis, N, col=0, row=0, cnt=0):
    global min_num

    vis = vis[:]
    vis[col] = True
    cnt += board[row][col]
    if cnt >= min_num:
        return False
        
    is_fin = True
    nxt = []
    for i in range(N):
        if not vis[i]:
            is_fin = False
            nxt.append(i)
    
    if is_fin:
        min_num = cnt
        return True
    
    for i in nxt:
        btk(vis, N, i, row + 1, cnt)


for case in range(1, int(input()) + 1):
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
    vis = [False] * N
    min_num = sum([board[i][0] for i in range(N)])

    for i in range(N):
        btk(vis, N, i)

    print(f'#{case} {min_num}')
