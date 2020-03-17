def sum_sequence(start, n):
    sub_total = start + (start + n - 1)
    if n % 2:
        result = sub_total * (n // 2) + sub_total // 2
    else:
        result = sub_total * (n // 2)
    return result


def idxtonum(x, y):
    return 1 + sum_sequence(1, y-1) + sum_sequence(y+1, x-1)


dp = [0] * 10001
for i in range(1, 141):
    for j in range(1, 142):
        temp = idxtonum(i, j)
        if temp <= 10000:
            dp[temp] = (i, j)

for case in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    x1, y1 = dp[p]
    x2, y2 = dp[q]
    print(f'#{case} {idxtonum(x1+x2, y1+y2)}')
