class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Count=[]
        for i in nums:
            if i in Count:
                return True
            else:
                Count.append(i)
        return False
        



         