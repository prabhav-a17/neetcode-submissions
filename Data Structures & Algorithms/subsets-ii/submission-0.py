class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #ok so what I'm thinking to remove duplicates we sort it and iterate 

        res=[]
        subset=[]
        nums.sort()

        def dfs(i):
            res.append(subset.copy())
            for x in range(i, len(nums)):
                if x>i and nums[x]==nums[x-1]:
                    continue
                subset.append(nums[x])
                dfs(x+1)
                subset.pop()
        dfs(0)
        return res
                
        dfs(0)
        return res
