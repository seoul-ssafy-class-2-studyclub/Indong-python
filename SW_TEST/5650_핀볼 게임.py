from pprint import pprint
from collections import deque, defaultdict

adj = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], 
[], [] ,[] ,[] ,[]]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
blackhole = tuple()
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
point = defaultdict(lambda: [])
for j in range(N):
    for i in range(N):
        if board[j][i] > 5:
            adj[board[j][i]].append((j, i))
        elif board[j][i] == -1:
            blackhole = (j, i)
        elif board[j][i] == 0:
            for k in range(4):
                point[(j, i)].append(k)
            
pprint(board)
print(adj)
print(point)
print(blackhole)

for key, value in point.items():
    for i in range(4):
        di = value[i]
        if di == -1:
            continue
        y, x = key
        yi, xi = y + delta[di][0], x + delta[di][1]
        while 0 <= yi < N and 0 <= xi < N and not board[yi][xi]:
            print((y, x), (yi, xi), di)
            point[(yi, xi)][di] = -1
            yi += delta[di][0]
            xi += delta[di][1]

print(point)

