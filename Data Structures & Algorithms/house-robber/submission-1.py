class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[]
        dp.append(nums[0])
        if len(nums)>1:
            dp.append(max(nums[0],nums[1]))

            for i in range(2, len(nums)):
                dp.append(max(dp[i-1], dp[i-2]+nums[i]))

        return dp[len(nums)-1]
        