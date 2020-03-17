for case in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        idx, num = map(int, input().split())
        arr.append(0)
        N += 1
        now = N - 1

        while now != idx:
            arr[now] = arr[now-1]
            now -= 1
        
        arr[idx] = num

    print('#{0} {1}'.format(case, arr[L]))
    