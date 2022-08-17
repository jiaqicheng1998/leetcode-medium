# Given an unsorted array of integers nums, return 
# the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence 
# is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

def longestConsecutive(nums):
    set_nums = set(nums)
    longest_len = 0

    for num in set_nums: 
        if num - 1 not in set_nums: #the only number inside the if statement is 100, 200, 1
            curr = num
            curr_len = 1

            while curr+1 in set_nums: #count consecutives from the smallest number possible
                curr_len += 1
                curr += 1
            longest_len = max(longest_len, curr_len)
    return longest_len
