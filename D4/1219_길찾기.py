adj = [[1, 2], [4, 3], [5, 9], [7], [3, 8], [7, 6], [10], [11], [], [8, 10], [], []]

vis = [False] * 12
stack = []
stack.append(0)
while stack:
    node = stack.pop()
    if not vis[node]:
        vis[node] = True:
        