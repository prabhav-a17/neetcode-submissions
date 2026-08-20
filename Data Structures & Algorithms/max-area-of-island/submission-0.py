
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Bruh this is just number of islands except instead of like counting the number of islands you just keep a count of the islands 

        #Ok so we started with 

        if not grid:
            return 0
        
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        max_Area=0

        def bfs(r, c):
            q=deque()
            visit.add((r,c))
            q.append((r,c))
            Area=1

            while q:
                row, col = q.popleft()
                directions= [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    nr,nc = dr + row, dc + col
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]==1 and (nr, nc) not in visit:
                        Area+=1
                        q.append((nr,nc))
                        visit.add((nr,nc))
            return Area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r, c) not in visit:
                    
                    max_Area= max(max_Area, bfs(r,c))

        return max_Area

