def dfs(node, adj, path, dp, vis):  
   
    vis[node] = True 
    
    if not adj[node]:
        path[node] = [node]

    for i in range(0, len(adj[node])):   
    
        if not vis[adj[node][i]]: 
            dfs(adj[node][i], adj, path, dp, vis)  
    
        dp[node] = max(dp[node], 1 + dp[adj[node][i]])
        if len(path[node]) < len([node] + path[adj[node][i]]):
            path[node] = [node] + path[adj[node][i]]
    

def findLongestPath(adj, n):  
   
    dp = [0] * (n + 1)  
    path = [[] for i in range(n + 1)]     
    vis = [False] * (n + 1) 

    for i in range(1, n + 1):   
        if not vis[i]:  
            dfs(i, adj, path, dp, vis)  

    ans = 0
    idx = 0    

    for i in range(1, n + 1):   
        if dp[i] > ans:
            ans = dp[i]
            idx = i
       
    return path[idx]
   
# # Driver Code  
# if __name__ == "__main__":  
   
#     n = 7
#     adj = [[] for i in range(n + 1)]
    
    
#     # Example-1  
#     addEdge(adj, 1, 2)  
#     addEdge(adj, 2, 3)  
#     addEdge(adj, 2, 4)  
#     addEdge(adj, 4, 3)  
#     addEdge(adj, 5, 1)
#     addEdge(adj, 6, 2)

    
#     print(findLongestPath(adj, n))


for case in range(1, int(input()) + 1):
    N = int(input())
    screws = list(map(int, input().split()))
    length = max(screws)
    ad_list = [[] for i in range(length + 1)]
    for i in range(0, (N*2) - 1, 2):
        ad_list[screws[i]].append(screws[i+1])
    line = findLongestPath(ad_list, length)
    result = []
    for i in range(len(line)):
        if i == 0 or i == len(line) - 1:
            result.append(line[i])
        else:
            result += [line[i]] * 2
    print(f'#{case} {" ".join(map(str, result))}')
    