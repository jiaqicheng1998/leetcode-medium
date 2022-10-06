# Given an integer array nums that may contain duplicates, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

def subsetsWithDup(nums):
    res = []
    nums.sort()

    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        dfs(i+1)

    dfs(0)
    return res
