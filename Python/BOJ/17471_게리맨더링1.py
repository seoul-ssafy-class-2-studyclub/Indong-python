from sys import stdin
from collections import deque


def powerset(k=2):
    global ans
    if k == N + 1:
        area1 = []
        area2 = []
        for i in range(1, N + 1):
            if t[i]:
                area1.append(i)
            else:
                area2.append(i)
        if not area1 or not area2:
            return

        def bfs(nodes):
            vis = [False] * (N + 1)
            queue = deque()
            queue.append(nodes[0])
            vis[nodes[0]] = True
            cnt = 1
            res = population[nodes[0]]
            while queue:
                node = queue.popleft()
                for nxt in adj[node]:
                    if not vis[nxt] and nxt in nodes:
                        queue.append(nxt)
                        vis[nxt] = True
                        cnt += 1
                        res += population[nxt]
            if cnt == len(nodes):
                return res
            else:
                return False


        s1 = bfs(area1)
        s2 = bfs(area2)
        if s1 and s2:
            ans = min(ans, abs(s1-s2))

    else:
        t[k] = 1
        powerset(k+1)
        t[k] = 0
        powerset(k+1)


input = stdin.readline
N = int(input())
population = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
for i in range(N):
    info = list(map(int, input().split()))
    for j in info[1:]:
        adj[i+1].append(j)

t = [0] * (N + 1)
t[1] = 1
ans = 987654321
powerset()
if ans == 987654321:
    ans = -1
print(ans)
