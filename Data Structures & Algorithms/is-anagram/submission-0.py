class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        newS= ''.join(sorted(s))
        newT= ''.join(sorted(t))
        if newT==newS: 
            return True
        else:
            return False

            
            
        