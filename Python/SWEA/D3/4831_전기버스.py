case_size = int(input())
for case in range(1, case_size + 1):
    bus = 0
    count = 0
    K, N, M = map(int, input().split())
    list_charge = list(map(int, input().split()))
    move = K
    while bus < N:
        if bus + move == N:
            break
        elif (bus + move) in list_charge:
            count += 1
            bus += move
            move = K
        else:
            move -= 1
            if move == 0:
                count = 0
                break
    print(f'#{case} {count}')
