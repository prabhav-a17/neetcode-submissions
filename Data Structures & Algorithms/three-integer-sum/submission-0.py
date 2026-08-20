class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedN= sorted(nums)
        res=[]
        
        for i, a in enumerate(sortedN):
            if a > 0:
                break
            if i>0 and a == sortedN[i-1]:
                continue
            l= i+1
            r =len(sortedN)-1
            while l<r:
                threeSum=a+ sortedN[l] + sortedN[r]
                if threeSum<0:
                    l+=1
                elif threeSum>0:
                    r-=1
                else:
                    res.append([a, sortedN[l], sortedN[r]])
                    l+=1
                    r-=1
                    while sortedN[l]== sortedN[l-1] and l<r:
                        l+=1
                    while l < r and sortedN[r] == sortedN[r+1]:
                        r -= 1
        return res

        