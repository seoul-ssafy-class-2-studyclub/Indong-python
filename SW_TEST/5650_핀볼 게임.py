def move(y, x, di):
    cnt = 0
    yi, xi = y + delta[di][0], x + delta[di][1]
    while True:
        while 0 <= yi < N and 0 <= xi < N and not board[yi][xi]:
            yi += delta[di][0]
            xi += delta[di][1]
            if yi == y and xi == x:
                return cnt
        cnt += 1
        if 0 > xi or 0 > yi or xi >= N or yi >= N:
            di = adj[5][di]
            yi += delta[di][0]
            xi += delta[di][1]
        else:
            com = board[yi][xi]
            if com == -1:
                cnt -= 1
                return cnt
            if com > 5:
                di = di
                cnt -= 1
                if adj[com][0] == (yi, xi):
                    yi, xi = adj[com][1]
                else:
                    yi, xi = adj[com][0]
                yi += delta[di][0]
                xi += delta[di][1]
            else:
                di = adj[com][di]
                yi += delta[di][0]
                xi += delta[di][1]
        if yi == y and xi == x:
            return cnt
        

for case in range(1, int(input()) + 1):
    adj = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2], [], [], [], [], []]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    blackhole = tuple()
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    point = []

    for j in range(N):
        for i in range(N):
            if board[j][i] > 5:
                adj[board[j][i]].append((j, i))
            elif board[j][i] == -1:
                blackhole = (j, i)
            elif board[j][i] == 0:
                point.append((j, i))

    max_score = 0
    for idx in point:
        for i in range(4):
            di = i
            y, x = idx
            score = move(y, x, di)
            if max_score < score:
                max_score = score

    print(f'#{case} {max_score}')
