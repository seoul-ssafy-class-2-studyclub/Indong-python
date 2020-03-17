def cnt(node):
    global res
    res += 1
    for nxt in child[node]:
        cnt(nxt)


def preorder(node):
    global flag
    if node == N:
        cnt(node)
        flag = True
    if flag:
        return
    for nxt in child[node]:
        preorder(nxt)
    

for case in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    parent = [0] * (E + 2)
    child = [[] for _ in range(E + 2)]
    edges = list(map(int, input().split()))
    res = 0
    flag = False
    for i in range(0, E * 2, 2):
        parent[edges[i+1]] = edges[i]
        child[edges[i]].append(edges[i+1])

    for i in range(1, E + 2):
        if not parent[i]:
            preorder(i)

    print(f'#{case} {res}')
