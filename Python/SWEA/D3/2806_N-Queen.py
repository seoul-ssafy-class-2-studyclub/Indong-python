def N_Queen(visit, N):
    global cnt
    v = len(visit)
    if v == N:
        cnt += 1
        return True

    nxt = list(range(N))
    for i in range(v):
        if visit[i] in nxt:
            nxt.remove(visit[i])
        left = visit[i] - v + i
        right = visit[i] + v - i
        if left >= 0 and left in nxt:
            nxt.remove(left)
        if right < N and right in nxt:
            nxt.remove(right)
        if not nxt:
            break

    if not nxt:
        return False

    for n in nxt:
        vis = visit[:]
        vis.append(n)
        N_Queen(vis, N)

for case in range(1, int(input()) + 1):
    N = int(input())
    cnt = 0
    for i in range(N):
        N_Queen([i], N)
    print(f'#{case} {cnt}')
    