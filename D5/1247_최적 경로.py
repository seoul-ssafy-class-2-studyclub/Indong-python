from collections import deque

def calc_dis(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


for case in range(1, int(input()) + 1):
    N = int(input())
    idx = list(map(int, input().split()))
    M = 1 << (N + 2)
    dp = [[0] * M for _ in range(N + 2)]
    dis = [[calc_dis(idx[x*2], idx[x*2+1], idx[y*2], idx[y*2+1]) for x in range(N + 2)] for y in range(N + 2)]
    
    queue = deque()
    for i in range(2, N + 2):
        nxt = 1 | (1 << i)
        dp[i][nxt] = dis[0][i]
        queue.append((i, nxt))

    for _ in range(N):
        for i in range(len(queue)):
            frm, cur = queue.popleft()
            if _ == N - 1:
                nxt = M - 1
                if not dp[1][nxt]:
                    dp[1][nxt] = dp[frm][cur] + dis[frm][1]
                else:
                    dp[1][nxt] = min(dp[1][nxt], dp[frm][cur] + dis[frm][1])
                continue

            for to in range(2, N + 2):
                if cur & (1 << to):
                    continue
                nxt = cur | (1 << to)
                val = dp[frm][cur] + dis[frm][to]
                if not dp[to][nxt]:
                    queue.append((to, nxt))
                    dp[to][nxt] = val
                elif dp[to][nxt] > val:
                    dp[to][nxt] = val
                    
    print(f'#{case} {dp[1][M-1]}')
