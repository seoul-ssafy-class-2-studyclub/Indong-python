def dfs(node, adj, path, vis, cnt=1):

    vis[node] -= 1

    path[cnt] = path[cnt-1] + [node]

    for i in range(0, len(adj[node])):
        if vis[adj[node][i]]:
            dfs(adj[node][i], adj, path, vis, cnt + 1)

def findpath(adj, vis, n):
    path = [[] for i in range(sum(vis) + 1)]
    is_possible = False

    for i in range(1, n + 1):
        visit = vis[:]
        if visit[i]:
            dfs(i, adj, path, visit)
        if len(path[-1]) == sum(vis):
            is_possible = True
            break
    print(is_possible)
    return path


adj = [[], [1, 2], [3, 4], [1, 2], [3, 4]]
vis = [0, 1, 2, 3, 4]

print(findpath(adj, vis, 4))