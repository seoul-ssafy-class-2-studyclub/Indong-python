# adj = [[], [2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]
# vis = [None, 1, 1, 1, 0, 2, 2, 1, 0, 1]

for case in range(1, 11):
    V, E = map(int, input().split())
    vis = [None] + [0] * V
    adj = [[] for i in range(V + 1)]
    graph = list(map(int, input().split()))

    for i in range(0, len(graph) - 1, 2):
        adj[graph[i]].append(graph[i+1])
        vis[graph[i+1]] += 1

    path = ''
    for i in range(len(vis)):
        if vis[i] != 0:
            continue
        stack = []
        stack.append(i)
        while stack:
            node = stack.pop()
            if vis[node] > 0:
                vis[node] -= 1
            if vis[node] == 0:
                path += str(node) + ' '
                vis[node] = 'Fin'
                stack.extend(adj[node])

    print(f'#{case} {path.rstrip()}')
