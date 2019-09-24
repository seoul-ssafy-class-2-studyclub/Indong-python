for case in range(1, int(input()) + 1):
    btr = list(map(int, input().split()))
    N = btr[0]
    dp = [False] * N
    for i in range(N - 1, 0, -1):
        if N <= i + btr[i]:
            dp[i] = 1
        elif not btr[i]:
            dp[i] = 0
        else:
            dp[i] = min([dp[i+j] for j in range(1, btr[i] + 1) if dp[i+j]]) + 1
    print(f'#{case} {dp[1] - 1}')
