from sys import stdin
from collections import deque


def monkey(K):
    queue = deque()
    queue.append((0, 0, K, 0))
    vis[0][0] |= 1 << K

    while queue:
        y, x, k, cnt = queue.popleft()
        if y == H - 1 and x == W - 1:
            return cnt
        status = 4 if k == 0 else 12
        for i in range(status):
            yi = y + dxy[i][0]
            xi = x + dxy[i][1]
            if 0 <= yi < H and 0 <= xi < W and not board[yi][xi]:
                if i >= 4:
                    if not vis[yi][xi] & (1 << k - 1):
                        vis[yi][xi] |= 1 << (k - 1)
                        queue.append((yi, xi, k-1, cnt+1))
                else:
                    if not vis[yi][xi] & (1 << k):
                        vis[yi][xi] |= 1 << k
                        queue.append((yi, xi, k, cnt+1))
    return -1


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
input = stdin.readline
K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
vis = [[0] * W for _ in range(H)]
ans = monkey(K)
print(ans)
