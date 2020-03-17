for case in range(1, int(input()) + 1):
    prices = list(map(int, input().split()))
    year = list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        day = prices[0] * year[i-1]
        month = prices[1]
        three = 99999
        if i >= 3:
            three = prices[2]
        dp[i] = min(dp[i-1] + day, dp[i-1] + month, dp[i-3] + three)
    
    res = dp[12]
    if res > prices[3]:
        res = prices[3]

    print(f'#{case} {res}')
