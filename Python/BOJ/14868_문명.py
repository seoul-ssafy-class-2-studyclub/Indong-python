from sys import stdin


def find(x):
    if x == root[x]:
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
        size[y] += size[x]
    else:
        root[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    return True


input = stdin.readline
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, K = map(int, input().split())
world = [[0] * N for _ in range(N)]
civilization = []
root = [i for i in range(K + 1)]
rank = [1] * (K + 1)
size = [1] * (K + 1)
for c in range(1, K + 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    world[y][x] = c
    civilization += [(y, x)]


