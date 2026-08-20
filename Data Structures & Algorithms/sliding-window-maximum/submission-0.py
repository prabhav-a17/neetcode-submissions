class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l= 0
        r=k-1
        list=[]
        while r< len(nums):
            newList = nums[l:r+1]
            list.append(max(newList))
            l+=1
            r+=1
        return list
        
