class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Ok so I gotta see for each of these like whether it will go all the way to the other side
        #Ok so the top right corner and the bottom left corner are always gonna be there
        #Ok so 

        Rows= len(heights)
        Cols=len(heights[0])
        pac=set()
        atl=set()
        def dfs(c,r,visit,heightVal):
            if r in range(Rows) and c in range(Cols) and (r,c) not in visit and heights[r][c] >= heightVal:
                visit.add((r,c))
                dfs(c-1,r,visit,heights[r][c])
                dfs(c+1,r,visit,heights[r][c])
                dfs(c,r-1,visit,heights[r][c])
                dfs(c,r+1,visit,heights[r][c])

        for r in range(Rows):
            dfs(0, r, pac, heights[r][0])
            dfs(Cols-1, r, atl, heights[r][Cols-1])
        for c in range(Cols):
            dfs(c, 0, pac, heights[0][c])
            dfs(c, Rows-1, atl, heights[Rows-1][c])
        res=[]
        for r in range(Rows):
            for c in range(Cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res



