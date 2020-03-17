def dfs(node, adj, dp, vis):  
   
    # Mark as visited  
    vis[node] = True 
    
    # Traverse for all its children  
    for i in range(0, len(adj[node])):   
    
        # If not visited  
        if not vis[adj[node][i]]: 
            dfs(adj[node][i], adj, dp, vis)  
    
        # Store the max of the paths  
        dp[node] = max(dp[node], 1 + dp[adj[node][i]])  
    
# Function to add an edge  
def addEdge(adj, u, v):  
   
    adj[u].append(v)  
    
# Function that returns the longest path  
def findLongestPath(adj, n):  
   
    # Dp array  
    dp = [0] * (n + 1)  
      
    # Visited array to know if the node  
    # has been visited previously or not  
    vis = [False] * (n + 1) 
      
    # Call DFS for every unvisited vertex  
    for i in range(1, n + 1):   
        if not vis[i]:  
            dfs(i, adj, dp, vis)  
       
    ans = 0 
    
    # Traverse and find the maximum of all dp[i]  
    for i in range(1, n + 1):   
        ans = max(ans, dp[i])  
       
    return ans  
   
# Driver Code  
if __name__ == "__main__":  
   
    n = 5 
    adj = [[] for i in range(n + 1)]
    
    # Example-1  
    addEdge(adj, 1, 2)  
    addEdge(adj, 1, 3)  
    addEdge(adj, 3, 2)  
    addEdge(adj, 2, 4)  
    addEdge(adj, 3, 4)  
    
    print(findLongestPath(adj, n)) 