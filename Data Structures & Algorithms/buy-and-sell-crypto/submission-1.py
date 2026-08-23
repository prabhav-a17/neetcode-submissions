class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        currMin=prices[0]
        

        for x in prices:
            maxP=max(maxP,x-currMin)
            currMin=min(x, currMin)

        return maxP

        