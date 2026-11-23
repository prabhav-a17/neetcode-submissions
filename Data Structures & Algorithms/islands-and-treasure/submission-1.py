class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Ok so here what can we do 
        #Start at a land cell run bfs until we get to the treasure chesr
        #Keep a count for how long that takes
        # Then we backtrack upon that and then keep decreasing and we do this for every land cell im assuming and if one is less than what it was before we use that 
        #Instead of starting at all the land cells why dont we start at all the treasure chests and then for each run of bfs we change the count of those that should be easier to implement 

        rows= len(grid)
        cols= len(grid[0])
        visited=set()

        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            
            
            while q:

                ro, co= q.popleft()
                distance = grid[ro][co]+1
                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    r= ro+dr
                    c= co + dc 

                    if (r in range(rows) and c in range(cols) and grid[r][c] > 0 and grid[r][c] > distance):
                        grid[r][c]=distance
                        q.append((r,c))
                        


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]==0:
                    visited.add((r,c))
                    bfs(r,c)

