from sys import stdin
input = stdin.readline
def main():
    dp = [0] + [99999] * K
    for i in range(N):
        coin = int(input())
        if coin > K:
            continue
        for j in range(coin, K + 1):
            dp[j] = min(dp[j-coin] + 1, dp[j])

    if dp[K] == 99999:
        print(-1)
    else:
        print(dp[K])


N, K = map(int, input().split())
main()
