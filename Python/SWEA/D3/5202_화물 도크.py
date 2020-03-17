for case in range(1, int(input()) + 1):
    N = int(input())
    app = [list(map(int, input().split())) for _ in range(N)]
    app.sort(key=lambda x: x[1])
    cnt = 1
    end = app[0][1]
    for i in range(1, N):
        if app[i][0] >= end:
            cnt += 1
            end = app[i][1]
    print(f'#{case} {cnt}')
