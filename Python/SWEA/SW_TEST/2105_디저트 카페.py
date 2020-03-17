# 우하 -> 좌하 -> 좌상 -> 우상 순서로 진행한다.
delta = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
 
 
def dfs(y, x, vis, di=0, cnt=0):
    global max_cnt
    global start
    # 디저트 종류의 중복을 확인하기 위해 vis를 복사해 온다.
    vis = vis[:]
    vis[board[y][x]] = True
    cnt += 1
    # 좌상(2) 방향으로 진행 중일 때는 시작점과 현재 지점의 기울기가 1이어야만 방향을 전환할 수 있다.
    if di == 2:
        if x + y == start[0] + start[1]:
            di = [3]
        else:
            di = [2]
    # 우상(3) 방향일 때는 다른 방향으로 바꿀 수 없다.
    elif di == 3:
        di = [3]
    # 우하(0)일 때는 우하(0), 좌하(1) / 좌하(1)일 때는 좌하(1), 좌상(2)으로만 갈 수 있다.
    else:
        di = [di, di + 1]
 
    for d in di:
        xi = x + delta[d][0]
        yi = y + delta[d][1]
        # 만약 다음 지점이 시작점과 같다면 기존 최댓값과 경로 길이를 비교한다.
        if (yi, xi) == start:
            if max_cnt < cnt:
                max_cnt = cnt
            return True
        # 다음 지점에서 판매 중인 디저트가 아직 구매 전이라면 재귀 호출을 실시한다.
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
    