from sys import stdin
input = stdin.readline

N = int(input())
workday = [0] * (N + 1)
pay = [0] * (N + 1)
dp = [0] * (N + 1)
for i in range(N):
    wi, pi = map(int, input().split())
    workday[i] = wi
    pay[i] = pi

for i in range(N - 1, -1, -1):
    if workday[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], (pay[i] + dp[i+workday[i]]))

print(dp[0])
