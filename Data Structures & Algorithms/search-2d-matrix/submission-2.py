class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        


        rows= len(matrix)
        cols= len(matrix[0])

        low=0
        high=(rows*cols)-1

        while low <= high:

            mid=(low+(high))//2
            
            row, col= divmod(mid, cols)
            mid_value= matrix[row][col]

            if mid_value==target:
                return True

            elif mid_value < target:
                low= mid+1
            else:
                high=mid-1
        return False



        




