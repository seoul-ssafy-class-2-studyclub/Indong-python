for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    interval = N // 4
    password = input()
    cand = set()

    for _ in range(interval):
        for i in range(0, N - 1, interval):
            cand.add(int(password[i:i+interval], 16))
        password = password[-1] + password[:-1]
    cand = sorted(list(cand), reverse=True)
    print(f'#{case} {cand[K-1]}')
