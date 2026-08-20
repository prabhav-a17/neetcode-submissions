class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        Rows, Cols = len(matrix), len(matrix[0])

        t=0
        b=Rows-1

        while t<=b:
            midR= (t+b)//2

            if target > matrix[midR][-1]:
                t= midR+1
            elif target < matrix[midR][0]:
                b= midR-1
            else:
                break
        
        if not t <= b:
            return False
        
        row= (t+b)//2

        l=0
        r=Cols-1

        while l<=r:
            mid = (l+r)//2

            if target==matrix[row][mid]:
                return True

            if target> matrix[row][mid]:
                l=mid+1
            else:
                r= mid-1

        return False