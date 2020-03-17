from sys import stdin

def dfs(y, x, total, k=1):
    global res
    if k == 4:
        if res < total:
            res = total
        return

    for dy, dx in dxy:
        yi = y + dy
        xi = x + dx
        if 0 <= yi < N and 0 <= xi < M and not vis[yi][xi]:
            vis[yi][xi] = True
            dfs(yi, xi, total+paper[yi][xi], k+1)
            vis[yi][xi] = False


def chk_cross(y, x):
    temp = []
    # ㅗ
    if y >= 1 and x < M - 2:
        temp.append(sum(paper[y][x:x+3]) + paper[y-1][x+1])
    # ㅜ 
    if y < N - 1 and x < M - 2:
        temp.append(sum(paper[y][x:x+3]) + paper[y+1][x+1])
    # ㅓ
    if y < N - 2 and x >= 1:
        temp.append(sum([paper[i][x] for i in range(y, y+3)]) + paper[y+1][x-1])
    # ㅏ
    if y < N - 2 and x < M - 1:
        temp.append(sum([paper[i][x] for i in range(y, y+3)]) + paper[y+1][x+1])
    if temp:
        return max(temp)
    return 0


dxy = [(-1, 0), (0, 1), (1, 0)]
input = stdin.readline
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
vis = [[False] * M for _ in range(N)]

res = 0
for r in range(N):
    for c in range(M):
        res = max(chk_cross(r, c), res)
        vis[r][c] = True
        dfs(r, c, paper[r][c])        
        vis[r][c] = False

print(res)
