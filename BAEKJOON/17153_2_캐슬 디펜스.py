from itertools import combinations
from heapq import heappop, heappush

def calc_dis(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

N, M, D = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(N)]

enemies = [(r, c, False) for c in range(M) for r in range(N) if game[r][c]]
size = len(enemies)
res = 0

for x, y, z in combinations(range(M), 3):
    targets = enemies[:]
    for i in range(N):
        t_x, t_y, t_z = [], [], []
        for r, c, dead in targets:
            if dead:
                continue



    

        
        

# a = []
# heappush(a, 1)
# heappush(a, 2)
# for i in range(2):
#     a[i] += 1

# print(heappop(a))

