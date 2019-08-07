def dfs(node, adj, dp, visit):
    visit[node] = True

    for i in range(0, len(adj[node]))


def find(adj, n):

    dp = [0] * (n + 1)

    visit = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visit[i]:
            dfs(i, adj, dp, visit)

    ans = 0

    for i in range(1, n + 1):
        if dp[i] > ans:
            ans = dp[i]

    return ans