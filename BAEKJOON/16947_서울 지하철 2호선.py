import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(node, past):
    if chk[node] == 1:
        return node
    
    chk[node] = 1

    for nxt in adj[node]:
        if nxt == past:
            continue
        res = dfs(nxt, node)
        if res == -2:
            return -2
        if res >= 0:
            chk[node] = 2
            if node == res:
                return -2
            else:
                return res
    return -1


input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N + 1)]
chk = [False] * (N + 1)

for i in range(N):
    s1, s2 = map(int, input().split())
    adj[s1].append(s2)
    adj[s2].append(s1)

dfs(1, 0)
queue = deque()
res = [-1] * (N + 1)
for i in range(1, N + 1):
    if chk[i] == 2:
        res[i] = 0
        queue.append(i)

while queue:
    node = queue.popleft()
    for nxt in adj[node]:
        if res[nxt] == -1:
            res[nxt] = res[node] + 1
            queue.append(nxt)

print(' '.join(map(str, res[1:])))

# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)

# def dfs(node, start, path, line=0):
#     vis[node] = True
#     for nxt in adj[node]:
#         if nxt != start and not vis[nxt]:
#             temp = path + [nxt]
#             dfs(nxt, start, temp, line+1)
#         elif nxt == start and line >= 2:
#             for i in path:
#                 chk[i] = True
#             return True


# input = sys.stdin.readline
# N = int(input())
# adj = [[] for _ in range(N + 1)]
# chk = [False] * (N + 1)

# for i in range(N):
#     s1, s2 = map(int, input().split())
#     adj[s1].append(s2)
#     adj[s2].append(s1)

# for i in range(1, N + 1):
#     if chk[i]:
#         continue
#     vis = [False] * (N + 1)
#     for node in adj[i]:
#         if chk[node]:
#             continue
#         dfs(node, i, [i, node], 1)
#         break

# res = [0] * (N + 1)
# for i in range(1, N + 1):
#     if not chk[i]:
#         continue
#     queue = deque()
#     for nxt in adj[i]:
#         if not chk[nxt]:
#             queue.append((nxt, 1))
#             res[nxt] = 1
#     while queue:
#         node, dis = queue.popleft()
#         for nxt in adj[node]:
#             if not chk[nxt] and not res[nxt]:
#                 queue.append((nxt, dis + 1))
#                 res[nxt] = dis + 1

# print(' '.join(map(str, res[1:])))