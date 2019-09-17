def work(vis, N, frm=0, cnt=0, k=0):
    global min_num

    if k == N - 1:
        cnt += green[frm][0]
        if not min_num:
            min_num = cnt
        elif min_num > cnt:
            min_num = cnt
        return True

    for i in range(N):
        if not vis[i]:
            visit = vis[:]
            visit[i] = True
            nxt = cnt
            nxt += green[frm][i]
            if min_num and nxt >= min_num:
                continue
            work(visit, N, i, nxt, k + 1)

for case in range(1, int(input()) + 1):
    N = int(input())
    green = []
    for _ in range(N):
        green.append(list(map(int, input().split())))
    vis = [False] * N
    vis[0] = True
    min_num = 0
    work(vis, N)
    print('#{0} {1}'.format(case, min_num))
    