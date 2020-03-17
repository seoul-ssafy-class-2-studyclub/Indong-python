def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

    
for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    classmate = list(map(int, input().split()))
    root = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    for i in range(0, M * 2, 2):
        union(classmate[i], classmate[i+1])
    
    cnt = set()
    for i in range(1, N + 1):
        cnt.add(find(i))

    print(f'#{case} {len(cnt)}')
