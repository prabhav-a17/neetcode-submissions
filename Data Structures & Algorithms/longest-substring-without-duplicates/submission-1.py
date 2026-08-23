class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       #Ok so here we have to use a sliding window 
       #Let me psuedo code it 
       #Ok so first we need our objects
       #Max Length and whats been seen and curr window length
       #Ok now first we keep increasing our window as much as we can until we get something that has been seen twice and then once this is seen twice keep shrinking the window until there are no duplicates
       #And then we keep increasing the window until we reach this issue of containing a duplicate again

       #Wait thinking about it why do we need to remove anything why dont we just shift over one with the max that we currently have and then we will be good
       if s=="":
            return 0 
       seen=set()
       maxWin=1

       l=0
       r=1
       seen.add(s[l])

       while r < len(s):
            while s[r] in seen and l < r:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxWin=max(len(seen), maxWin)
            r+=1

       return maxWin
    #[a,b,b,a]
    #seen:{a,b}