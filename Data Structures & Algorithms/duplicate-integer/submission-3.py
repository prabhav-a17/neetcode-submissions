class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_M= {}
        for x in nums:
            if x not in hash_M:
                hash_M[x]=1
            else:
                return True
        return False


         