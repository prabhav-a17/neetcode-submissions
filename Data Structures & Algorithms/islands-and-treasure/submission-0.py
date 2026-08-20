class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited=set()
        rows=len(grid)
        cols=len(grid[0])
        q=deque()

        def addRoom(r,c):
            if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] != -1:
                visited.add((r,c))
                q.append((r,c))
            


        for r in range(rows):
            for c in range (cols):
                if grid[r][c]==0 and (r,c) not in visited:
                    q.append([r,c])
                    visited.add((r,c))
                    
        dist=0
        while q:
            for i in range(len(q)):
                r,c =q.popleft()
                grid[r][c]= dist
                addRoom(r-1,c)
                addRoom(r+1,c)
                addRoom(r,c-1)
                addRoom(r,c+1)
            dist+=1


            
        