class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList={i:[] for i in range(n)}

        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        visited=set()
        dfs_count=0
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nxt in adjList[node]:
                dfs(nxt)
        
        for i in range(n):
            if i not in visited:
                dfs_count+=1
                dfs(i)
        return dfs_count
                


