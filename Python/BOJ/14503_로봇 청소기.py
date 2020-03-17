import sys

def clean(r, c, d):
    global res
    di = adj[d][0]
    ri = r + dy[di]
    ci = c + dx[di]
    cnt = 0
    while cnt < 4 and (vis[ri][ci] or room[ri][ci]):
        cnt += 1
        di = adj[di][0]
        ri = r + dy[di]
        ci = c + dx[di]

    if cnt == 4:
        di = d
        ri = r + dy[adj[di][1]]
        ci = c + dx[adj[di][1]]
        if room[ri][ci]:
            return 0, 0, 0, True
    else:
        vis[ri][ci] = True
        res += 1
    
    return ri, ci, di, False

        
# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# [왼쪽 방향, 후진]
adj = [[3, 2], [0, 3], [1, 0], [2, 1]]
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]
vis[r][c] = True

res = 1
is_fin = False
while not is_fin:
    r, c, d, is_fin = clean(r, c, d)

print(res)
