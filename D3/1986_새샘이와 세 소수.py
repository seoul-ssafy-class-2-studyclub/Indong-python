primes_chk = [True] * 1000

for i in range(2, int(1000 ** 0.5) + 1):
    if primes_chk[i] == True:
        for j in range(i + i, 1000, i):
            primes_chk[j] = False

primes = [num for num in range(2, 1000) if primes_chk[num] == True]
primes_count = len(primes)


case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    idx = len(primes) - 1
    count = 0
    for i in range(primes_count):
        if primes[i] > N:
            idx = i
            break

    for i in range(idx):
        for j in range(i, idx):
            prime_std = primes[i] + primes[j]
            if N - prime_std < primes[j]:
                break
            for k in range(j, idx):
                prime_sum = prime_std + primes[k]
                if prime_sum > N:
                    break
                if prime_sum == N:
                    count += 1
                    break
    print(f'#{case} {count}')
