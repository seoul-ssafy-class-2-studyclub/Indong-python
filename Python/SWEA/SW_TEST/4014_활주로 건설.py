def chk_airstrip(road, N, X):
    last = road[0]
    temp = road[0]
    cnt = 1
    chk = False
    for i in range(1, N):
        # print(f'#{i}: last:{last}, temp:{temp}, a[i]:{a[i]}')
        if not chk:
            if last == road[i]:
                cnt += 1
            elif road[i] == last + 1:
                if cnt < X:
                    return 0
                last, temp = road[i], road[i]
                cnt = 1
            elif road[i] == last - 1:
                cnt = 1
                temp = road[i]
                chk = True
            else:
                return 0
        else:
            if temp == road[i]:
                cnt += 1
                if cnt >= X:
                    cnt = 0
                    last = temp
                    chk = False
            if temp != road[i] and cnt < X:
                return 0
    if temp != last:
        return 0

    return 1


for case in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    board = []
    result = 0
    for i in range(N):
        road = list(map(int, input().split()))
        result += chk_airstrip(road, N, X)
        board.append(road)

    for c in range(N):
        road = []
        for r in range(N):
            road.append(board[r][c])
        result += chk_airstrip(road, N, X)

    print(f'#{case} {result}')
