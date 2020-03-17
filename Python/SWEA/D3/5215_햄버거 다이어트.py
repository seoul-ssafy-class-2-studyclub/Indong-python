def best_recipe(node, happy, kcal, limit, vis):
    global ing
    global adj
    global max_happy

    vis = vis[:]
    vis[node] = True
    happy += ing[node][0]
    kcal += ing[node][1]
    
    if happy > max_happy:
        max_happy = happy

    for i in range(len(adj[node])):
        if kcal + ing[adj[node][i]][1] <= limit:
            best_recipe(adj[node][i], happy, kcal, limit, vis)


for case in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    adj = [[]]
    ing = [[]]
    max_happy = 0
    visit = [False] * (N + 1)
    for i in range(N):
        adj.append([i for i in range(i + 2, N + 1)])
    for i in range(N):
        ing.append(list(map(int, input().split())))
    for i in range(1, N + 1):
        best_recipe(i, 0, 0, L, visit)
    print(f'#{case} {max_happy}')
