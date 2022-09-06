# Suppose an array of length n sorted in ascending order is 
# rotated between 1 and n times. For example, the array nums 
# = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., 
# a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], 
# a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, 
# return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

# determine in the left sorted array or right sorted array

def findMin(nums):
    if len(nums) == 1: return nums[0]
    l = 0
    r = len(nums) - 1

    while l <= r:
        pivot = (r + l) // 2
        if pivot == l: return min(nums[l], nums[l + 1])
        elif pivot == r: return min(nums[r], num[r - 1])
        elif nums[pivot] > nums[r] and nums[pivot] > nums[l]:
            l = pivot
        else:
            r = pivot
    return nums[-1]

print(findMin([11,13,15,17]))
print(findMin([3,4,5,6,7,1,2]))
print(findMin([2,3,1]))