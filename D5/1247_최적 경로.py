def working(vis, dis, frm, to, cnt=0):
    global min_dis
    global N

    vis = vis[:]
    vis[to] = True
    cnt += 1
    dis += abs(idx[frm][0] - idx[to][0]) + abs(idx[frm][1] - idx[to][1])
    if min_dis <= dis:
        return False
    if cnt == N:
        dis += abs(idx[to][0] - idx[1][0]) + abs(idx[to][1] - idx[1][1])
        if min_dis > dis:
            min_dis = dis
            return True
        else:
            return False
    for i in range(2, N + 2):
        if not vis[i]:
            working(vis, dis, to, i, cnt)


for case in range(1, int(input()) + 1):
    N = int(input())
    idx = list(map(int, input().split()))
    vis = [False] * (N + 2)
    for i in range(N + 2):
        idx.append([idx.pop(0), idx.pop(0)])
    
    min_dis = 99999999
    for i in range(2, N + 2):
        working(vis, 0, 0, i)

    print('#{0} {1}'.format(case, min_dis))
