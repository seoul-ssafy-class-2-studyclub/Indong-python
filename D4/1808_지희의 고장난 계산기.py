def chk_digit(num):
    cnt = 0
    while num > 0:
        digit = num % 10
        if not button[digit]:
            return False
        num //= 10
        cnt += 1
    return cnt


def mk_factor(num):
    dig = chk_digit(num)
    if dig:
        dp[num] = dig
        return dp[num]
    
    res = 987654321
    square_root = int(num ** 0.5)
    factors = [i for i in range(2, square_root + 1) if not num % i]
    for fac in factors:
        val1 = mk_factor(fac)
        val2 = mk_factor(num // fac)
        if val1 and val2:
            res = min(res, val1 + val2 + 1)

    if res != 987654321:
        dp[num] = res
        return res


primes_chk = [True] * (10 ** 6 + 1)
for i in range(2, 10 ** 3 + 1):
    if primes_chk[i]:
        for j in range(i + i, 10 ** 6 + 1, i):
            primes_chk[j] = False

result_list = []
T = int(input())
for case in range(T):
    button = list(map(int, input().split()))
    number = int(input())
    dp = [False] * (number + 1)
    res = mk_factor(number)
    if res == None:
        res = -1
    else:
        res += 1
    result_list.append(res)

for case in range(T):
    print(f'#{case + 1} {result_list[case]}')
