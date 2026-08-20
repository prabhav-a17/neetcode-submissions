class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_p= max(piles)

        l=1
        u=max_p
        res=u

        while l <= u:
            mid= (l+u)//2
            totalTime=0

            for p in piles:
                totalTime += math.ceil(float(p)/mid)
            if totalTime <= h:
                res=mid
                u= mid-1
            else:
                l=mid+1
        return res