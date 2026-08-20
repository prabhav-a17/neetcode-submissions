class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def dfs(i, curr, total):
            if total==target:
                res.append(curr.copy()) #because we are passing around a variable in reference so its like kinda cooked.
                return
            if total > target or i >= len(candidates):
                return

            #include candates[i]

            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()

            #skip candidates[i] we need to skip all the duplicate numbers
            while i+1< len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, curr, total)

        dfs(0,[],0)
        return res
