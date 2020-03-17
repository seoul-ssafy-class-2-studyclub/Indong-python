dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for case in range(1, int(input()) + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    dp = [[set([board[y][x]]) for x in range(4)] for y in range(4)]
    res = set()

    for i in range(6):
        temp = [[set() for _ in range(4)] for _ in range(4)]
        for y in range(4):
            for x in range(4):
                for num in dp[y][x]:
                    nxt = num * 10
                    for dy, dx in dxy:
                        yi = y + dy
                        xi = x + dx
                        if 0 <= yi < 4 and 0 <= xi < 4:
                            if i == 5:
                                res.add(nxt + board[yi][xi])
                            else:
                                temp[yi][xi].add(nxt + board[yi][xi])
        dp = [row[:] for row in temp]

    print(f'#{case} {len(res)}')
