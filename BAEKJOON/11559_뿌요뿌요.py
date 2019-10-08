from sys import stdin
from collections import deque

# input = stdin.readline
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move():
    for c in range(6):
        for r in range(11, -1, -1):
            if game[r][c] != '.':
                for k in range(11, r, -1):
                    if game[k][c] == '.':
                        game[r][c], game[k][c] = game[k][c], game[r][c]
                        break


def main():
    chain = 0
    flag = True
    while flag:
        vis = [[False] * 6 for _ in range(12)]
        flag = False
        for r in range(12):
            for c in range(6):
                if game[r][c] == '.' or vis[r][c]:
                    continue
                color = game[r][c]
                queue = deque()
                queue.append((r, c))
                puyo = [(r, c)]
                chk = 1
                vis[r][c] = True
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in dxy:
                        yi = y + dy
                        xi = x + dx
                        if 0 <= yi < 12 and 0 <= xi < 6 and game[yi][xi] == color and not vis[yi][xi]:
                            queue.append((yi, xi))
                            puyo.append((yi, xi))
                            chk += 1
                            vis[yi][xi] = True
                if chk >= 4:
                    flag = True
                    for y, x in puyo:
                        game[y][x] = '.'
        if flag:
            chain += 1
        
        move()
    return chain


game = [list(input()) for _ in range(12)]
res = main()

print(res)
