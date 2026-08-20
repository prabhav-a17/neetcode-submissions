class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = set()
        for x in nums:
            if x not in dict:
                dict.add(x)
            else:
                return True
        return False
         