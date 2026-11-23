class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        

        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        maxArea=0



        def bfs(r,c):
            q=collections.deque()
            visited.add((r,c))
            q.append((r,c))
            count=1

            while q:
                ro, co = q.popleft()
                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    r = ro+ dr
                    c= co + dc

                    if (r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
                        count+=1

            return count


        

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    area=bfs(r,c)
                    maxArea=max(area, maxArea)

        return maxArea