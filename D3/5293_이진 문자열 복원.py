def dfs(node, adj, path, vis, cnt=1):
    visit = vis[:]
    visit[node] -= 1
    path[cnt] = path[cnt-1] + [node]

    for i in range(0, len(adj[node])):
        if visit[adj[node][i]]:
            dfs(adj[node][i], adj, path, visit, cnt + 1)


def findpath(adj, vis, n):
    length = sum(vis)
    path = [[] for i in range(length + 1)]
    is_possible = False
    

    for i in range(1, n + 1):
        visit = vis[:]
        if visit[i]:
            dfs(i, adj, path, visit)
        if len(path[-1]) == length:
            is_possible = True
            break
    if is_possible:
        return path[-1]
    else:
        return False


adj = [[], [1, 2], [3, 4], [1, 2], [3, 4]]

for case in range(1, int(input()) + 1):
    vis = [0] + list(map(int, input().split()))
    result = ''
    path_list = findpath(adj, vis, 4)
    if path_list:
        for i in range(len(path_list)):
            if path_list[i] <= 2:
                result += '0'
            else:
                result += '1'
        if path_list[-1] % 2 == 0:
            result += '1'
        else:
            result += '0'
        print(f'#{case} {result}')
    else:
        print(f'#{case} impossible')
