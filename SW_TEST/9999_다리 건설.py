from collections import deque


def chk_bridge(idx1, idx2):
    y1, x1, y2, x2 = idx1
    b1, a1, b2, a2 = idx2
    if (x1 <= a2 and x2 >= a1) or x1 == a1 or x2 == a2:
        if y2 < b1:
            dis = b1 - y2 - 1
        else:
            dis = y1 - b2 - 1
        return True, dis
    elif (y1 <= b2 and y2 >= b1) or y1 == b1 or y2 == b2:
        if x2 < a1:
            dis = a1 - x2 - 1
        else:
            dis = x1 - a2 - 1
        return True, dis
    else:
        return False, 0
        

def construction(k=0, cnt=1, cost=0):
    global min_cost
    if cnt == n:
        if cost < min_cost:
            min_cost = cost
        return True

    cand = []
    for i in range(n):
        if not vis[i]:
            pos, dis = chk_bridge(island_idx[k], island_idx[i])
            if pos and dis:
                cand.append((i, dis))
    # print(vis)
    # print(k, cand)
    cd = len(cand)
    for i in range(1 << cd):
        temp = []
        for j in range(cd):
            if i & (1 << j):
                temp.append(cand[j])
        
        expense = 0
        for idx, exp in temp:
            vis[idx] = True
            expense += exp
        for idx, exp in temp:
            construction(idx, cnt+len(temp), cost+expense)
        for idx, exp in temp:
            vis[idx] = False


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # N = 9
    # board = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
    # [1, 1, 1, 1, 1, 1, 1, 1, 1],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 1, 1, 1],
    # [1, 1, 1, 1, 0, 0, 1, 1, 1],
    # [1, 1, 1, 1, 0, 0, 1, 1, 1],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    # N = 7
    # board = [
    # [1, 0, 0, 0, 0, 0, 1],
    # [1, 0, 0, 0, 0, 0, 1],
    # [1, 0, 0, 1, 0, 0, 1],
    # [0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 1, 0, 0, 0],
    # [0, 0, 0, 1, 0, 0, 0],
    # [0, 0, 0, 1, 0, 0, 0]]
    chk = [row[:] for row in board]
    island_idx = []
    for r in range(N):
        for c in range(N):
            if chk[r][c]:
                island = [r, c]
                queue = deque()
                queue.append((r, c))
                chk[r][c] = 0
                while queue:
                    y, x = queue.popleft()
                    for b, a in delta:
                        yi = y + b
                        xi = x + a
                        if 0 <= yi < N and 0 <= xi < N and chk[yi][xi]:
                            chk[yi][xi] = 0
                            queue.append((yi, xi))
                island += [y, x]
                island_idx.append(island)

    n = len(island_idx)
    vis = [False] * n
    vis[0] = True
    min_cost = 9999999999999
    construction()

    if min_cost == 9999999999999:
        print(f'#{case} {min_cost}')
    else:
        print(f'#{case} {min_cost}')
