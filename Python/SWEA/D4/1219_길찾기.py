# adj = [[1, 2], [4, 3], [5, 9], [7], [3, 8], [7, 6], [10], [], [], [8, 10], [], []]

def dfs(adj):
    vis = [False] * 100
    stack = []
    stack.append(0)
    while stack:
        node = stack.pop()
        if not vis[node]:
            vis[node] = True
            if 99 in adj[node]:
                return 1
            stack.extend(adj[node])
    return 0


for i in range(10):
    case, N = map(int, input().split())
    graph = list(map(int, input().split()))
    adj = [[] for i in range(100)]
    for i in range(0, (N * 2) - 1, 2):
        adj[graph[i]].append(graph[i+1])
    print(f'#{case} {dfs(adj)}')
