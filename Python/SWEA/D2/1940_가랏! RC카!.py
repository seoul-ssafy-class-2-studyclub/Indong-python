case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    v = 0
    distance = 0
    for command in range(N):
        c_list = list(map(int, input().split()))
        if c_list[0] == 1:
            v += c_list[1]
        elif c_list[0] == 2:
            v -= c_list[1]
            if v < 0:
                v = 0
        distance += v
    print(f'#{case} {distance}')
