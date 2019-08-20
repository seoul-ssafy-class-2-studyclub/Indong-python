# word = '()()((()))'
# word2 = '((()((((()()((()())((())))))'
# def gwalho(word):
#     left = '('
#     right = ')'
#     stack = []

#     for i in word:
#         if i == left:
#             stack.append(i)
#         elif i == right:
#             if stack.pop() != left:
#                 return False
#     if stack:
#         return False
#     return True

# print(gwalho(word2))
# graph = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# adj_list = [[] for i in range(8)]
# adj_matrix = [[0] * 8 for i in range(8)]
# for i in range(0, len(graph), 2):
#     adj_list[graph[i]].append(graph[i+1])
#     adj_list[graph[i+1]].append(graph[i])
#     adj_matrix[graph[i]][graph[i+1]] = 1
#     adj_matrix[graph[i+1]]

adj = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]
vis = [False] * 8
stack = []
stack.append(1)
path = []

while stack:
    node = stack.pop()
    if not vis[node]:
        path += [node]
        vis[node] = True
        # for i in range(len(a)):
            
        stack.extend(adj[node])

print('-'.join(map(str, path)))