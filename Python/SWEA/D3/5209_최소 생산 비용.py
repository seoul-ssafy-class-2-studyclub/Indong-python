def btk(p=0, cost=0):
    global res
    if res < cost:
        return
    if p == N:
        if cost < res:
            res = cost
        return
    for i in range(N):
        if not vis[i]:
            vis[i] = True
            btk(p+1, cost + factory[p][i])
            vis[i] = False


for case in range(1, int(input()) + 1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    vis = [False] * N
    res = 987654321
    btk()
    print(f'#{case} {res}')
    