class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        n = len(nums)//2

        if nums[n] == target:
            return n
        elif nums[n]>target:
            new_nums=nums[:n]
            result= self.search(new_nums, target)
            return result
        elif nums[n]< target:
            new_nums=nums[n+1:]
            result=self.search(new_nums, target)
            return n + 1 + result if result != -1 else -1
        else:
            return -1



        