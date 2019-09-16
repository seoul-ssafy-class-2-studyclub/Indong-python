def my_permutation(pro=1, k=0):
    global max_pro
    if k == N:
        if pro > max_pro:
            max_pro = pro
            return True
    for i in range(N):
        if not vis[i]:
            temp = pro * (pro_arr[k][i] / 100)
            if temp != 0 and (not max_pro or temp > max_pro):
                vis[i] = True
                my_permutation(temp, k+1)
                vis[i] = False

for case in range(1, int(input()) + 1):
    N = int(input())
    pro_arr = [list(map(int, input().split())) for _ in range(N)]
    vis = [False] * N
    max_pro = 0
    my_permutation()
    print(f'#{case} {max_pro * 100:.6f}')
