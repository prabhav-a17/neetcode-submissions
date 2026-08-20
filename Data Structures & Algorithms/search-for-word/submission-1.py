class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Ok so what I am thinking is dfs right and then if we start from like A and check first if its the first character the thing if it is we go to either dfs on the next one and then add one to the index and check that and do the same for that and keep doing it ?
        Rows, Cols= len(board), len(board[0])
        path=set() #to keep track of visited
        def dfs(x,y,index):
            if index==len(word):
                return True
            if (x<0 or y<0 or x>= Rows or y>= Cols or board[x][y]!= word[index] or (x,y) in path):
                return False
            path.add((x,y))
            res= (dfs(x+1,y,index+1) or
                    dfs(x-1,y,index+1)or 
                    dfs(x,y+1,index+1)or 
                    dfs(x,y-1,index+1))
            path.remove((x,y))
            return res

        for x in range(Rows):
            for y in range(Cols):
                if dfs(x,y,0):
                    return True
        return False
            
