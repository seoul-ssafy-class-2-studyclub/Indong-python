for case in range(1, int(input()) + 1):
    N = int(input())
    M = int(input())
    INF = float('inf')
    adj = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        adj[a][b] = 1
    
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if adj[i][k] != INF and adj[k][j] != INF:
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

    chk = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if adj[i][j] != INF:
                chk[i] += 1
                chk[j] += 1
    
    res = chk.count(N - 1)
    print(f'#{case} {res}')
        