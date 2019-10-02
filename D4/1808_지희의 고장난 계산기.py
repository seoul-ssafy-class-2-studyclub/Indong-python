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
        return dig + 1
 
    square_root = int(num ** 0.5)
    factors = [i for i in range(2, square_root + 1) if not num % i]
    prime = []
    for fac in factors:
        val1 = chk_digit(fac)
        val2 = chk_digit(num // fac)
        if val1:
            dp[fac] = val1
            prime.append(fac)
        if val2:
            dp[num//fac] = val2
            prime.append(num//fac)
    prime.sort(reverse=True)

    res = -1
    l = len(prime)
    for i in range(l):
        new = num
        temp = 0
        for j in range(i, l):
            p = prime[j]
            while not new % p:
                new //= p
                temp += dp[p] + 1
        if new > 1:
            continue
        if res == -1 or res > temp:
            res = temp

    return res


result_list = []
T = int(input())
for case in range(T):
    button = list(map(int, input().split()))
    number = int(input())
    dp = [False] * (number + 1)
    res = mk_factor(number)
    result_list.append(res)

for case in range(T):
    print(f'#{case + 1} {result_list[case]}')
