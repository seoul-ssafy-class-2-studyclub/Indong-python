from sys import stdin
from collections import defaultdict

def spring_summer_winter():
    global cnt
    for r in range(N):
        for c in range(N):
            nour = board[r][c]
            if forest[r][c]:
                temp = defaultdict(lambda: 0)
                energy = 0
                for tree, num in sorted(forest[r][c].items()):
                    alive = min(nour // tree, num)
                    dead = num - alive
                    if alive > 0:
                        nour -= tree * alive
                        temp[tree + 1] = alive
                    
                    energy += (tree // 2) * dead
                    cnt -= dead
                nour += energy
                forest[r][c] = temp
            
            nour += A[r][c]
            board[r][c] = nour

        
def fall():
    global cnt
    for r in range(N):
        for c in range(N):
            trees = forest[r][c]
            if trees:
                for tree, num in trees.items():
                    spread = 0
                    if tree % 5 == 0 and num != 0:
                        spread += num
                    if spread:
                        for x, y in dxy:
                            xi = c + x
                            yi = r + y
                            if 0 <= xi < N and 0 <= yi < N:
                                forest[yi][xi][1] += spread
                                cnt += spread


N, M, K = map(int, stdin.readline().split())
board = [[5] * N for _ in range(N)]
forest = [[defaultdict(lambda: 0) for _ in range(N)] for _ in range(N)]
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
dxy = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
cnt = 0

for _ in range(M):
    y, x, old = map(int, stdin.readline().split())
    forest[y-1][x-1][old] += 1
    cnt += 1

for i in range(K):
    spring_summer_winter()
    fall()

print(cnt)

