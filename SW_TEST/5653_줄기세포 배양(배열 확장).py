delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    vessel = [list(map(int, input().split())) for _ in range(N)]
    cells = []
    all = 0
    alive = 0
    for r in range(N):
        for c in range(M):
            vit = vessel[r][c]
            if vit:
                vessel[r][c] = [vit, vit, vit, 0]
                cells.append([r, c])
                all += 1
                alive += 1

    for time in range(1, K + 1):
        for i in range(all):
            r, c = cells[i]
            if vessel[r][c][0] > 0:
                vessel[r][c][0] -= 1
                continue
            if vessel[r][c][0] != 0:
                continue
            act, vit, life, pre = vessel[r][c]
            for b, a in delta:
                ri = r + b
                ci = c + a
                if ri < 0:
                    vessel = [[0] * M] + vessel
                    ri += 1
                    r += 1
                    N += 1
                    for j in cells:
                        j[0] += 1
                elif ri >= N:
                    vessel += [[0] * M]
                    N += 1
                if ci < 0:
                    for y in range(N):
                        vessel[y] = [0] + vessel[y]
                    ci += 1
                    c += 1
                    M += 1
                    for j in cells:
                        j[1] += 1
                elif ci >= M:
                    for y in range(N):
                        vessel[y] += [0]
                    M += 1
                if not vessel[ri][ci]:
                    vessel[ri][ci] = [vit, vit, vit, time]
                    cells.append([ri, ci])
                    alive += 1
                    all += 1
                elif vessel[ri][ci][3] == time and vessel[ri][ci][2] < vit:
                    vessel[ri][ci] = [vit, vit, vit, time]
            vessel[r][c][2] -= 1
            if vessel[r][c][2] == 0:
                vessel[r][c][0] = -1
                alive -= 1

    print(f'{case} {alive}')
            