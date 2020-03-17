for case in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    for i in range(E):
        frm, to = map(int, input().split())
        adj[frm].append(to)
        adj[to].append(frm)
    S, G = map(int, input().split())
    vis = [False] * (V + 1)

    queue = [S]
    vis[S] = True
    can_move = False
    cnt = 0
    while queue and not can_move:
        cnt += 1
        for i in range(len(queue)):
            node = queue.pop(0)
            for j in adj[node]:
                if j == G:
                    can_move = True
                    break
                if not vis[j]:
                    queue.append(j)
                    vis[j] = True
    if can_move:
        print('#{0} {1}'.format(case, cnt))
    else:
        print('#{0} {1}'.format(case, 0))
