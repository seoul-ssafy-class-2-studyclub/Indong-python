import sys
from collections import defaultdict, deque
   
class Graph: 
   
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = defaultdict(set)
        self.Time = 0
   
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].add(v) 
        self.graph[v].add(u) 
   
    '''A recursive function that find articulation points  
    using DFS traversal 
    u --> The vertex to be visited next 
    visited[] --> keeps tract of visited vertices 
    disc[] --> Stores discovery times of visited vertices 
    parent[] --> Stores parent vertices in DFS tree 
    ap[] --> Store articulation points'''
    def APUtil(self, u, visited, ap, parent, low, disc): 
  
        #Count of children in current node  
        children = 0
  
        # Mark the current node as visited and print it 
        visited[u] = True
  
        # Initialize discovery time and low value 
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
  
        #Recur for all the vertices adjacent to this vertex 
        for v in self.graph[u]: 
            # If v is not visited yet, then make it a child of u 
            # in DFS tree and recur for it 
            if visited[v] == False : 
                parent[v] = u 
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc) 
  
                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                low[u] = min(low[u], low[v]) 
  
                # u is an articulation point in following cases 
                # (1) u is root of DFS tree and has two or more chilren. 
                if parent[u] == -1 and children > 1: 
                    ap[u] = True
  
                #(2) If u is not root and low value of one of its child is more 
                # than discovery value of u. 
                if parent[u] != -1 and low[v] >= disc[u]: 
                    ap[u] = True    
                      
                # Update low value of u for parent function calls     
            elif v != parent[u]:  
                low[u] = min(low[u], disc[v]) 
  
  
    #The function to do DFS traversal. It uses recursive APUtil() 
    def AP(self): 
   
        # Mark all the vertices as not visited  
        # and Initialize parent and visited,  
        # and ap(articulation point) arrays 
        visited = [False] * (self.V) 
        disc = [float("Inf")] * (self.V) 
        low = [float("Inf")] * (self.V) 
        parent = [-1] * (self.V) 
        ap = [False] * (self.V) #To store articulation points 
  
        # Call the recursive helper function 
        # to find articulation points 
        # in DFS tree rooted with vertex 'i' 
        for i in range(self.V): 
            if visited[i] == False: 
                self.APUtil(i, visited, ap, parent, low, disc) 

        return ap, parent
  

def bfs(r, c, cur):
    pacific[r][c] = num
    queue = deque()
    queue.append((r, c))
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            yi = y + dy
            xi = x + dx
            if 0 <= yi < N and 0 <= xi < M:
                nxt = pacific[yi][xi]
                if pacific[yi][xi] == cur:
                    queue.append((yi, xi))
                    pacific[yi][xi] = num


input = sys.stdin.readline
N, M = map(int, input().split())
pacific = [list(input().strip()) for _ in range(N)]
num = 1
is_island = [False]
for r in range(N):
    for c in range(M):
        if pacific[r][c] == '#' or pacific[r][c] == '.':
            if pacific[r][c] == '#':
                is_island += [True]
            else:
                is_island += [False]
            bfs(r, c, pacific[r][c])
            num += 1

adj = Graph(num)
for r in range(N):
    for c in range(M):
        cur = pacific[r][c]
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ri = r + dr
            ci = c + dc
            if 0 <= ri < N and 0 <= ci < M:
                nxt = pacific[ri][ci]
                if cur != nxt:
                    adj.addEdge(cur, nxt)

ap, parent = adj.AP()
safe = [True] * num

for i in range(1, num):
    if not safe[i]:
        continue
    if is_island[i] and ap[i]:
        stack = deque()
        stack.append(i)
        while stack:
            node = stack.pop()
            for nxt in adj.graph[node]:
                if not safe[nxt] or nxt == parent[node]:
                    continue
                stack.append(nxt)
                safe[nxt] = False

for r in range(N):
    for c in range(M):
        num = pacific[r][c]
        if not is_island[num]:
            pacific[r][c] = '.'
        elif not safe[num]:
            pacific[r][c] = 'X'
        else:
            pacific[r][c] = 'O'
    print(''.join(pacific[r]))
