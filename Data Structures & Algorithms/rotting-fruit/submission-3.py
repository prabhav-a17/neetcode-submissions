class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        q=collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2 and (r,c) not in visited:
                    visited.add((r,c))
                    q.append((r,c))
        
        min=0
        while q:
            for i in range(len(q)):
                ro, co = q.popleft()
                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    r = dr + ro 
                    c = dc + co

                    if (r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited):
                        grid[r][c]=2
                        visited.add((r,c))
                        q.append((r,c))
            min+=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        return max(0,min-1)





