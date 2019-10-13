from sys import stdin
from collections import deque

input = stdin.readline
def find_parent():
    stack = deque()
    stack.append((1, 0))
    while stack:
        node, parent = stack.pop()
        vis[node] = True
        tree[node] = parent
        for nxt in adj[node]:
            if not vis[nxt]:
                stack.append((nxt, node))


N = int(input())
adj = [[] for _ in range(N + 1)]
vis = [False] * (N + 1)
tree = [0] * (N + 1)
for i in range(N - 1):
    node1, node2 = map(int, input().split())
    adj[node1].append(node2)
    adj[node2].append(node1)

find_parent()

for i in range(2, N + 1):
    print(tree[i])
