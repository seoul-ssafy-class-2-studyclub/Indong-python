from sys import stdin


# def find(x):
#     if x == root[x]:
#         return x
#     root[x] = find(root[x])
#     return root[x]


# def union(x, y):
#     x = find(x)
#     y = find(y)

#     if x == y:
#         return False

#     if rank[x] < rank[y]:
#         root[x] = y
#     else:
#         root[y] = x
#         if rank[x] == rank[y]:
#             rank[x] += 1
#     return True


def check():
    for i in range(N):
        for j in range(N):
            if i != j and costs[i][j] == INF:
                return -1

    ans = 0
    for n1, n2 in res_edges:
        ans += costs[n1][n2]
    return ans

    
input = stdin.readline
INF = float('inf')
N = int(input())
weights = [list(map(int, input().split())) for _ in range(N)]
edges = []
for i in range(N - 1):
    for j in range(i + 1, N):
        if weights[i][j]:
            edges.append((i, j, weights[i][j]))

edges.sort(key=lambda x: x[2])
# root = [i for i in range(N)]
# rank = [0] * N
costs = [[INF] * N for _ in range(N)]

res_edges = []
for n1, n2, w in edges:
    if costs[n1][n2] > w:
        costs[n1][n2] = w
        costs[n2][n1] = w
        res_edges.append((n1, n2))
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                costs[i][j] = min(costs[i][j], costs[i][n1] + costs[n1][j], costs[i][n2] + costs[n2][j])
                costs[j][i] = costs[i][j]

ans = check()
print(ans)
