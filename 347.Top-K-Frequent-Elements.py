# Given an integer array nums and an integer k, return 
# the k most frequent elements. You may return the answer 
# in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

def topKFrequent(nums, k):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    sorted_tuples = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return [t[0] for t in sorted_tuples][:k]

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
