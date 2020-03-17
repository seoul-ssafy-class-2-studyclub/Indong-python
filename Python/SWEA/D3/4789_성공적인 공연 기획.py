def buying(aud):
    N = len(aud)
    acc_sum = [0] * (N + 1)
    count = 0
    for i in range(N):
        acc_sum[i+1] = aud[i] + acc_sum[i]
        if i >= N - 1:
            continue
        if i + 1 > acc_sum[i+1]:
            diff = i + 1 - acc_sum[i+1]
            acc_sum[i+1] += diff
            count += diff
    return count
    
for case in range(1, int(input()) + 1):
    audience = [int(i) for i in input()]
    print(f'#{case} {buying(audience)}')
