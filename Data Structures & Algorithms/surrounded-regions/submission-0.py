class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #Ok so we keep going until we get Os surrounded by Xs and Xs only.
        #So what I am thinking is why dont I introduce like an empty array
        #And then every position of the O will be added to that array
        #Once I am done with the bfs we will change all the values in the array to Xs

        Rows= len(board)
        Cols = len(board[0])
        visited=set()
        
        def search(r,c,region):
            
            if r not in range(Rows) or c not in range(Cols) or board[r][c] != 'O' or (r,c) in visited:
                return 
            visited.add((r,c))
            region.append((r,c))
            search(r-1,c, region)
            search(r+1,c, region)
            search(r,c-1, region)
            search(r,c+1, region)
                
           

        
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c]=='O' and (r,c) not in visited:
                    region=[]
                    search(r,c,region)
                    is_surrounded=True
                    for x,y in region:
                        if x == 0 or x == Rows - 1 or y == 0 or y == Cols - 1.:
                            is_surrounded= False
                            break
                    if is_surrounded:
                        for x,y in region:
                            board[x][y]='X'
       


                    