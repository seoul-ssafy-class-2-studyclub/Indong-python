from collections import deque

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    vis = [False] * (N + 1)
    for i in range(M):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    cnt = 0
    for i in range(1, N + 1):
        if vis[i]:
            continue
        cnt += 1
        stack = deque()
        stack.append(i)
        while stack:
            node = stack.pop()
            vis[node] = True
            for j in adj[node]:
                if not vis[j]:
                    stack.append(j)

    print(f'#{case} {cnt}')
