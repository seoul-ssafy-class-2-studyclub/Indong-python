def cd(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


delta = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
for case in range(1, int(input()) + 1):
    M, A = map(int, input().split())
    idx = [0] * (A + 1)
    rng = [0] * (A + 1)
    temp = [0] * (A + 1)
    BC = [[0] * (A + 1) for _ in range(A + 1)]
    p1 = [1, 1]
    p2 = [10, 10]
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    for i in range(1, A + 1):
        x, y, c, p = list(map(int, input().split()))
        idx[i] = (y, x)
        rng[i] = c
        temp[i] = p
        BC[0][i] = p

    for i in range(1, A + 1):
        for j in range(i, A + 1):
            if i == j:
                BC[i][j] = temp[i]
            else:
                BC[i][j] = temp[i] + temp[j]
                
    result = 0
    for i in range(M + 1):
        cand_A = [0]
        cand_B = [0]
        bat = 0
        for j in range(1, A + 1):
            b, a = idx[j]
            y1, x1 = p1
            y2, x2 = p2 
            if cd(x1, y1, a, b) <= rng[j]:
                cand_A.append(j)
            if cd(x2, y2, a, b) <= rng[j]:
                cand_B.append(j)

        for k in range(len(cand_A)):
            for l in range(len(cand_B)):
                a, b = cand_A[k], cand_B[l]
                if a > b:
                    a, b = b, a
                if bat < BC[a][b]:
                    bat = BC[a][b]
        result += bat
        
        if i == M:
            break
        p1[0] += delta[move_A[i]][0]
        p1[1] += delta[move_A[i]][1]
        p2[0] += delta[move_B[i]][0]
        p2[1] += delta[move_B[i]][1]

    print(f'#{case} {result}')
