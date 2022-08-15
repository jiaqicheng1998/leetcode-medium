# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

def maxSubArray(nums):
    curr_sum = 0
    max_sub = nums[0]
    for i in nums:
        curr_sum = curr_sum + i
        max_sub = max(curr_sum, max_sub)
        if curr_sum < 0:
            curr_sum = 0
    return max_sub

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))
print(maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))
