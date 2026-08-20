class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Ok so this is similar to Course Schedule obviously where we were looking for cycle detection
        #Catch here we are returning not whether its possible to do the courses but we are returning 
        #The order of the courses so we can take a similar approach I am assuming except now we have to look at order
        
        preMap= {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited=set()
        visiting=set()
        res=[]

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
            
                