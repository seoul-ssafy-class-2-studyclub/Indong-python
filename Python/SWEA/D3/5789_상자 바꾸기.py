for case in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    box_list = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box_list[j] = i

    print(f'#{case} {" ".join(map(str, box_list))}')
