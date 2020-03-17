from collections import deque
from sys import stdin

input = stdin.readline
N, M = map(int, input().split())
classroom = [list(input().strip()) for _ in range(N)]
vis = [[[[False] * 3 for _ in range(4)] for _ in range(M)] for _ in range(N)]

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
flag = False
start = (0, 0)
for r in range(N):
    for c in range(M):
        if classroom[r][c] == 'S':
            start = (r, c)
        elif classroom[r][c] == 'C' and not flag:
            classroom[r][c] = 'D'
            flag = True

ans = 987654321
queue = deque()
queue.append((start[0], start[1], 0, 0, 0))
while queue:
    cur = queue.popleft()
    for i in range(4):
        if cur[2] == i and cur[4] > 0:
            continue
        ny = cur[0] + dxy[i][0]
        nx = cur[1] + dxy[i][1]
        status = cur[3]
        time = cur[4] + 1
        if 0 <= ny < N and 0 <= nx < M:
            if classroom[ny][nx] == '#' or vis[ny][nx][i][status]:
                continue
            if classroom[ny][nx] == 'C':
                if status == 2:
                    ans = min(ans, time)
                    continue
                else:
                    status = 1
            elif classroom[ny][nx] == 'D':
                if status == 1:
                    ans = min(ans, time)
                    continue
                else:
                    status = 2
            vis[ny][nx][i][status] = True
            queue.append((ny, nx, i, status, time))

if ans == 987654321:
    print(-1)
else:
    print(ans)
