prime_chk = [False] * 2 + [True] * ((10 ** 6) - 1)

for i in range(int((10 ** 6) ** 0.5) + 1):
    if prime_chk[i]:
        for j in range(i + i, (10 ** 6) + 1, i):
            prime_chk[j] = False

primes = [str(i) for i in range((10 ** 6) + 1) if prime_chk[i]]


for case in range(1, int(input()) + 1):
    D, A, B = map(int, input().split())
    D = str(D)
    cnt = 0
    for i in primes:
        if int(i) < A:
            continue
        if int(i) > B:
            break
        if D in i:
            cnt += 1
    print(f'#{case} {cnt}')
