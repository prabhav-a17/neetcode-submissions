class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Set = {}

        for i,n in enumerate(nums):
            diff= target - n
            if diff in Set:
                return [Set[diff], i]
            Set[n] = i 


        
        