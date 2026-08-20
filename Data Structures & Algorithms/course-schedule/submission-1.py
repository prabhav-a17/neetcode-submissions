class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Ok this question is basically asking for cycle detection
        #SO you basically are runnign a dfs and then if you encounter one that you have seen before you cooked
        preMap= {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited=set()

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs]==[]:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
