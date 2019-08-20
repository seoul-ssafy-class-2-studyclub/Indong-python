for case in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for i in range(V + 1)]
    vis = [False] * (V + 1)
    result = 0

    for i in range(E):
        n, m = map(int, input().split())
        adj[n][m] = 1
    S, G = map(int, input().split())
    stack = [S]
    
    while stack:
        node = stack.pop()
        if not vis[node]:
            vis[node] = True
            for i in range(V + 1):
                if adj[node][i]:
                    if i == G:
                        result = 1
                        stack = []
                        break
                    stack.append(i)
                    
    print(f'#{case} {result}')
