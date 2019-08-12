h = [[100, 200],
[300, 500],
[250, 300],
[500, 1000],
[400, 400]]

result = []
adj = [[], [2, 3, 4, 5], [3, 4, 5], [4, 5], [5], []]
visit = [False] + 6

vis = visit[:]
path = []
vis[1] == True
path += [1]

stack = []
stack += adj[1]

node = stack.pop()

print(stack)