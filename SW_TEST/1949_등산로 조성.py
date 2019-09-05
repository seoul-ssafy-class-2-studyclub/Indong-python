dt = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(y, x, k, cnt=1):
    global max_cnt
    now = mountain[y][x]
    for b, a in dt:
        yi = y + b
        xi = x + a
        if 0 <= yi < N and 0 <= xi < N:
            nxt = mountain[yi][xi]
            if nxt < now:
                mountain[y][x] = 100
                dfs(yi, xi, k, cnt+1)
                mountain[y][x] = now
            elif k and nxt - k < now:
                mountain[yi][xi] = now - 1
                mountain[y][x] = 100
                dfs(yi, xi, 0, cnt+1)
                mountain[yi][xi] = nxt
                mountain[y][x] = now
            else:
                if max_cnt < cnt:
                    max_cnt = cnt


for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    altitude = 0
    peaks = []
    for j in range(N):
        for i in range(N):
            temp = board[j][i]
            if temp > altitude:
                altitude = temp
                peaks = [(j, i)]
            elif temp == altitude:
                peaks.append((j, i))

    max_cnt = 0
    for i in range(len(peaks)):
        mountain = [row[:] for row in board]
        y, x = peaks[i]
        dfs(y, x, K)

    print(f'#{case} {max_cnt}')
