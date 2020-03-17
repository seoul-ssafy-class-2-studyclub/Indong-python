from collections import deque

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    vis = [False] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    queue = deque([(1, 0)])
    vis[1] = True
    cnt = 0
    while queue:
        node, dis = queue.popleft()
        for i in adj[node]:
            if not vis[i]:
                vis[i] = True
                cnt += 1
                if dis == 1:
                    continue
                queue.append((i, dis + 1))

    print(f'#{case} {cnt}')
    