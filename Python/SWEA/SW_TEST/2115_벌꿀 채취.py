def subset_sum(n, idx):
    for i in range(M):
        if not n & (1 << i):
            nxt = n | (1 << i)
            if not subset[nxt]:
                subset[nxt] = [subset[n][0] + collect[i], subset[n][1] + collect[i] ** 2]
                if subset[nxt][0] <= C:
                    if profit[idx] < subset[nxt][1]:
                        profit[idx] = subset[nxt][1]
                    subset_sum(nxt, idx)
                    

for case in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    L = N - M + 1
    honey = [list(map(int, input().split())) for _ in range(N)]
    length = N ** 2
    profit = [0] * length
    for r in range(N):
        for c in range(L):
            subset = [[0, 0]] + [0] * (1 << M)
            collect = honey[r][c:c+M]
            subset_sum(0, r*N+c)

    res = 0
    for i in range(length - M):
        for j in range(i + M, length):
            temp = profit[i] + profit[j]
            if res < temp:
                res = temp

    print(f'#{case} {res}')
