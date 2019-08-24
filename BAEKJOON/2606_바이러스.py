V = int(input())
E = int(input())
adj = [[] for i in range(V + 1)]
vis = [False] * (V + 1)

for i in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

stack = [1]
cnt = -1
while stack:
    node = stack.pop()
    if not vis[node]:
        vis[node] = True
        cnt += 1
        stack.extend(adj[node])

print(cnt)
