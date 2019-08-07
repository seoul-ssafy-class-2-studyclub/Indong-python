def prize(m, total, cnt=0):
    global DP
    money = int(''.join(m))

    if DP[cnt] > money:
        return False
    DP[cnt] = money

    if cnt == total:
        return True

    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            swap = m[:]
            swap[i], swap[j] = swap[j], swap[i]
            prize(swap, total, cnt + 1)


for case in range(1, int(input()) + 1):
    M, C = input().split()
    M = [i for i in M]
    C = int(C)
    DP = [0] * (C + 1)
    prize(M, C)
    print(f'#{case} {DP[-1]}')
