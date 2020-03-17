for case in range(1, int(input()) + 1):
    N = int(input())
    good_day = []
    cnt = 0
    for i in range(N):
        good_day.append(int(input()) - 1)
    
    good_day.pop(0)
    while good_day:
        cnt += 1
        x = good_day[0]
        for i in range(x, good_day[-1] + 1, x):
            if i not in good_day:
                continue
            good_day.remove(i)

    print(f'#{case} {cnt}')
