from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
pipe = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
can_move = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
for case in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    u = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1
    queue = deque()
    queue.append((R, C, u[R][C]))
    u[R][C] = -1
    while L > 1:
        L -= 1
        for _ in range(len(queue)):
            y, x, sh = queue.popleft()
            for i in pipe[sh]:
                dy, dx = delta[i]
                yi = y + dy
                xi = x + dx
                if 0 <= yi < N and 0 <= xi < M and (u[yi][xi] in can_move[i]):
                    queue.append((yi, xi, u[yi][xi]))
                    cnt += 1
                    u[yi][xi] = -1
    print(f'#{case} {cnt}')
