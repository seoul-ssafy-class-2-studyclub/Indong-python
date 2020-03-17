for case in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        C = list(input().split())
        if C[0] == 'I':
            arr.insert(int(C[1]), int(C[2]))
            N += 1
        elif C[0] == 'D':
            del arr[int(C[1])]
            N -= 1
        elif C[0] == 'C':
            arr[int(C[1])] = int(C[2])
    if N <= L:
        print('#{0} -1'.format(case))
    else:
        print('#{0} {1}'.format(case, arr[L]))
