class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Ok not sure how to code this but from what I understand and remember 
        # But basically we start with a window of 1 and then a set of that 
        # Have a max value
        # And then we keep adding to the window and doing a computation with like the seen of each of the letters take the most and then see if we can subtract at most k of the other ones to get only that one letter left and basically we compute the max window

        maxWin=1
        l=0
        r=0
        countDict={}
        
        while r < len(s):
            if s[r] not in countDict:
                countDict[s[r]]=1
            else:
                countDict[s[r]]+=1

            maxCount=max(countDict.values())

            while (r-l+1)-maxCount > k:
                countDict[s[l]]-=1
                l+=1
                maxCount=max(countDict.values())
            maxWin=max((r-l+1), maxWin)
            r+=1
        return maxWin
            

        


        