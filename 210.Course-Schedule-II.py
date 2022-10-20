# There are a total of numCourses courses you have to take, 
# labeled from 0 to numCourses - 1. You are given an array 
# prerequisites where prerequisites[i] = [ai, bi] indicates 
# that you must take course bi first if you want to take 
# course ai.

# For example, the pair [0, 1], indicates that to take course 
# 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all 
# courses. If there are many valid answers, return any of them. 
# If it is impossible to finish all courses, return an empty array.

def findOrder(numCourses, prerequisites):

    # build adjacency list of prereqs
    preMap = { i: [] for i in range(numCourses) }
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
    
    # a course has 3 possible states:
    # visited -> crs has been added to output
    # visiting -> crs not added to output, but added to cycle
    # unvisited -> crs not added to output or cycle
    visit, cycle = set(), set()
    output = []
    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True
        
        cycle.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False
        
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True
    
    for crs in range(numCourses):
        if not dfs(crs): return []
    return output
        
