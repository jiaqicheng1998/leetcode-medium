# Given a string s, find the length of the longest 
# substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a 
# subsequence and not a substring.

#sliding window of one first

# def lengthOfLongestSubstring(s):
#     if s == "": return 0
#     curr_str = s[0]
#     curr_idx = 0
#     max_len = 1

#     while curr_idx < len(s):
#         if curr_idx + len(curr_str) == len(s):
#             break
        
#         if s[curr_idx + len(curr_str)] not in curr_str:
#             curr_str = s[curr_idx:curr_idx+len(curr_str)+1]
#             max_len = max(max_len, len(curr_str))
#         else:
#             curr_idx += 1
#             curr_str = s[curr_idx]
    
#     return max_len

# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
# print(lengthOfLongestSubstring("pwwkew"))

# popping from the left until there is no repeatition
def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res