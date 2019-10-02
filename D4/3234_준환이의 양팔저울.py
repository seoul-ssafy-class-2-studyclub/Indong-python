cube = [3 ** i for i in range(10)]
for case in range(1, int(input()) + 1):
    N = int(input())
    M = 3 ** N
    weight = list(map(int, input().split()))
    dp = [[0] * M for _ in range(N)]

    for i in range(N):
        nxt = cube[i]
        dp[0][nxt] = [weight[i], 0, 1]

    for i in range(1, N):
        for cur in range(M):
            if not dp[i-1][cur]:
                continue
            
            left, right, now = dp[i-1][cur]
            temp = cur
            for j in range(N):
                if not temp % 3:
                    nxt = cur + cube[j]
                    nxt_left = left + weight[j]
                    if dp[i][nxt]:
                        dp[i][nxt][2] += now
                    else:
                        dp[i][nxt] = [nxt_left, right, now]
                    nxt_right = right + weight[j]
                    if left >= nxt_right:
                        nxt = cur + cube[j] * 2
                        if dp[i][nxt]:
                            dp[i][nxt][2] += now
                        else:
                            dp[i][nxt] = [left, nxt_right, now]
                temp //= 3

    res = 0
    for i in range(M):
        if dp[N-1][i]:
            res += dp[N-1][i][2]         
    print(f'#{case} {res}')
