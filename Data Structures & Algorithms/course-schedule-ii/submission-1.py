class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()
        valid = []
        def dfs(course):
            if course in visited: return False
            if preMap[course] == []:
                if course not in valid:
                    valid.append(course)
                return True

            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visited.remove(course)
            preMap[course] = []
            valid.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
            if c not in valid: valid.append(c)
        return valid
        
        