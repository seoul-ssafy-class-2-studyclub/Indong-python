from collections import deque
 
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for case in range(1, int(input()) + 1):
    N = int(input())
    house = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    res = 0
    idx = N ** 2
 
    for r in range(N):
        for c in range(N):
            if not dp[r][c]:
                queue = deque()
                queue.append((r, c))
                while queue:
                    y, x = queue.popleft()
                    for b, a in dxy:
                        yi = y + b
                        xi = x + a
                        if 0 <= yi < N and 0 <= xi < N and house[yi][xi] == house[y][x] + 1:
                            if dp[yi][xi]:
                                dp[r][c] += dp[yi][xi] + 1
                            else:
                                dp[r][c] += 1
                                dp[yi][xi] += 1
                                queue.append((yi, xi))
            if dp[r][c] > res:
                res = dp[r][c]
                idx = house[r][c]
            elif dp[r][c] == res and idx > house[r][c]:
                res = dp[r][c]
                idx = house[r][c]
 
    print(f'#{case} {idx} {res + 1}')