from sys import stdin

N = int(stdin.readline())
dp = [0, 0, 1, 1]
if N >= 4:
    dp += [0] * (N - 3)
    for i in range(4, N + 1):
        dp[i] = dp[i-1] + 1
        if not i % 2:
            dp[i] = min(dp[i//2] + 1, dp[i])
        if not i % 3:
            dp[i] = min(dp[i//3] + 1, dp[i])

print(dp[N])
