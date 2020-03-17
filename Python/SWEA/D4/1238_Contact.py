for case in range(1, 11):
    N, start = map(int, input().split())
    graph = list(map(int, input().split()))
    V = max(graph) + 1
    adj = [[] for i in range(V)]
    vis = [False] * V
    for i in range(0, N, 2):
        adj[graph[i]].append(graph[i+1])
    
    queue = [start]
    vis[start] = True
    end = []
    while queue:
        temp = []
        for n in range(len(queue)):
            node = queue.pop(0)
            for i in adj[node]:
                if not vis[i]:
                    vis[i] = True
                    temp.append(i)
                    queue.append(i)
        if temp:
            end = temp[:]

    print(f'#{case} {max(end)}')
