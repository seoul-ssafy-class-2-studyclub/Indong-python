def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    
    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    return True


for case in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    root = [i for i in range(V + 1)]
    rank = [0] * (V + 1)
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    res = 0

    for n1, n2, w in edges:
        if union(n1, n2):
            res += w

    print(f'#{case} {res}')

