# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, 
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets 
# does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

def threeSum(nums):
    sorted_nums = sorted(nums)
    res = []

    for i in range(len(sorted_nums)):
        left = i + 1
        right = len(sorted_nums) - 1

        while left < right:
            if sorted_nums[left] + sorted_nums[right] == -sorted_nums[i]:
                res.append(tuple([sorted_nums[i], sorted_nums[left], sorted_nums[right]]))
                left += 1
                right -= 1
            elif sorted_nums[left] + sorted_nums[right] < -sorted_nums[i]:
                left += 1
            else:
                right -= 1
    temp_res = set(res)
    return [list(tu) for tu in temp_res]



print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,0,0,0]))
print(threeSum([-2,0,1,1,2]))