class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l= 0
        r= len(heights)-1
        maximum=0
        
        while r>l:
            if ((r-l) * min(heights[l], heights[r]))>maximum:
                maximum= ((r-l) * min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l+=1
            else:
                r -=1
        return maximum
            