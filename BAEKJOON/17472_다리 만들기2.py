import sys
from collections import deque
from pprint import pprint

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


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline
N, M = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
edges = set()
num = 2
for r in range(N):
    for c in range(M):
        if country[r][c] == 1:
            country[r][c] = num
            queue = deque([(r, c)])
            while queue:
                y, x = queue.popleft()
                for dy, dx in dxy:
                    yi = y + dy
                    xi = x + dx
                    if 0 <= yi < N and 0 <= xi < M and country[yi][xi] == 1:
                        country[yi][xi] = num
                        queue.append((yi, xi))
            num += 1

root = [i for i in range(num)]
rank = [0] * num
adj = [set() for _ in range(num)]

for r in range(N):
    c = 0
    cnt = 0
    past = country[r][0]
    while c < M - 1:
        c += 1
        now = country[r][c]
        if not now:
            cnt += 1
        elif now == past and cnt >= 1:
            cnt = 0
        elif now != past:
            if past == 0:
                cnt = 0
                past = now
            else:
                if cnt > 1:
                    edges.add((past, now, cnt))
                    adj[past].add(now)
                    adj[now].add(past)
                past = now
                cnt = 0

for c in range(M):
    r = 0
    cnt = 0
    past = country[0][c]
    while r < N - 1:
        r += 1
        now = country[r][c]
        if not now:
            cnt += 1
        elif now == past and cnt >= 1:
            cnt = 0
        elif now != past:
            if past == 0:
                cnt = 0
                past = now
            else:
                if cnt > 1:
                    edges.add((past, now, cnt))
                    adj[past].add(now)
                    adj[now].add(past)
                past = now
                cnt = 0

def chk_bridge():
    global edges
    vis = [False] * num
    stack = deque([2])
    while stack:
        node = stack.pop()
        if not vis[node]:
            vis[node] = True
            stack.extend(adj[node])

    if sum(vis) != num - 2:
        return -1
        
    edges = sorted(list(edges), key=lambda x: x[2])
    res = 0
    vis = [False] * num
    vis[0] = vis[1] = True
    for n1, n2, w in edges:
        if w < 2 or (vis[n1] and vis[n2]):
            continue
        if union(n1, n2):
            vis[n1] = True
            vis[n2] = True
            res += w

    print(res)
    pprint(country)
    print(edges)
    return res
        
    

res = chk_bridge()
print(res)