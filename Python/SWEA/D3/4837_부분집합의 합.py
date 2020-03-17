arr = [i for i in range(1, 13)]
m = len(arr)

for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    count = 0
    for i in range(1<<m):
        subset = []
        for j in range(m):
            if i & (1<<j):
                subset.append(arr[j])
            if len(subset) > N:
                break
        if len(subset) == N and sum(subset) == K:
            count += 1

    print(f'#{case} {count}')
