class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        Rows=len(grid)
        Cols=len(grid[0])
        q=deque()

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visited.add((r,c))
        def bfs(r, c):
            if r in range(Rows) and c in range(Cols) and (r, c) not in visited and grid[r][c]==1:
                grid[r][c]=2
                q.append((r,c))
                visited.add((r,c))


        
        mins=0
        while q:
            for i in range(len(q)):
                r, c= q.popleft()
                bfs(r-1,c)
                bfs(r+1,c)
                bfs(r,c-1)
                bfs(r,c+1)
            if q:
                mins+=1
        for row in grid:
            if 1 in row:
                return -1
        return mins


        