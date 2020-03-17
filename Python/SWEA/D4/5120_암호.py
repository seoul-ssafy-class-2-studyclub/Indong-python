def password(arr, n, m, k):
    idx = 0
    start = arr[0]
    for i in range(k):
        idx += m
        if idx > n:
            idx %= n
        if idx == n:
            arr.insert(idx, arr[idx-1] + start)
        else:
            arr.insert(idx, arr[idx-1] + arr[idx])
        n += 1

    arr.reverse()
    result = ' '.join(map(str, arr[:10]))
    return result

for case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#{0} {1}'.format(case, password(arr, N, M, K)))
