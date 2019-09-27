def calc_dis(idx1, idx2):
    y1, x1 = idx1
    y2, x2 = idx2
    return (abs(y1 - y2) + abs(x1 - x2)) * 2


def find_mineral(ene, cnt=0):
    global res
    if res < cnt:
        res = cnt
    for i in range(mineral):
        if not vis[i]:
            y, x = mineral_idx[i]
            energy = ene - calc_dis(robot_idx, mineral_idx[i])
            if energy < 0:
                continue
            vis[i] = True
            find_mineral(energy, cnt+board[y][x])
            vis[i] = False


N, M, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
robot_idx = (0, 0)
mineral_idx = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            robot_idx = (r, c)
        elif board[r][c]:
            mineral_idx.append((r, c))

mineral = len(mineral_idx)
vis = [False] * mineral
res = 0
find_mineral(C)
print(res)


