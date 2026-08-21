class Solution:
    def trap(self, height: List[int]) -> int:
        #SO what do I want to do here
        #I want to use twopointers yes
        #But how its like 
        #[3,1,3,1,3]
        l=0
        r=len(height)-1
        res=0
        leftMax=height[l]
        rightMax=height[r]

        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(height[l],leftMax)
                res+=leftMax-height[l]

            else:
                r-=1
                rightMax=max(height[r],rightMax)
                res+=rightMax-height[r]

        return res