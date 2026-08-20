class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Ok so I am assuming this is just dfs with backtracking and then if its too large just exit out of the loop if its exactly equal then I add it 
        #Oh but the same number can be chosen over and over again 
        # I mean that doesnt change too much right I can just choose to run dfs on the same one again its going to be extremely slow but I cant really think of anything better to do at the moment 
        res=[]
        subset=[]
        def dfs(i, subset, sums):
            #What is my base case
            if sums> target or i >= len(nums):
                return
            if sums==target:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i, subset, sums+nums[i])
            subset.pop()
            dfs(i+1, subset, sums)
        dfs(0,[], 0)
        return res

