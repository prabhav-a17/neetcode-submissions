class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        res=(9999999999999999999999999999999999999999999)
        
        while l <= r:

            if nums[l]<nums[r]:
                res=min(res,nums[l])
                break

                
            mid = (r+l)//2

            if nums[mid]>= nums[l]:
                res=min(nums[mid], res)
                l=mid+1
            else:
                res=min(nums[mid], res)
                r=mid-1

        return res