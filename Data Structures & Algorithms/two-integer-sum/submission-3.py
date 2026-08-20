class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
        for x in enumerate(nums):
            diff = target-x[1]
            if diff not in count:
                count[x[1]]=x[0]
            else:
                return [count[diff],x[0]]
            