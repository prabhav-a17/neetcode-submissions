class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows= len(grid)
        cols=len(grid[0])

        visited=set()
        islands=0

        def bfs(r, c):
            visited.add((r,c))
            q=collections.deque()
            q.append((r,c))

            while q:
                ro, co = q.popleft()

                for dr, dc in [[1,0], [0,1], [-1,0], [0,-1]]:
                    r= dr+ro
                    c= dc+ co

                    if (r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c]=='1'):
                        q.append((r,c))
                        visited.add((r,c))



        




        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=='1':
                    bfs(r,c)
                    islands+=1

        return islands
        

        