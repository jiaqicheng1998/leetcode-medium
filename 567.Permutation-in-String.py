# Given two strings s1 and s2, return true if s2 contains 
# a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations 
# is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# double for loop run time error
# def checkInclusion(s1, s2):
#     d = {}
#     for j in range(len(s1)):
#         d[s1[j]] = 1 + d.get(s1[j], 0)
#     length = len(s1)

#     for i in range(len(s2) - length + 1):
#         curr = s2[i:i+length]
#         curr_d = {}
#         for m in range(len(curr)):
#             curr_d[curr[m]] = 1 + curr_d.get(curr[m], 0)
#         if curr_d == d:
#             return True
    
#     return False

# print(checkInclusion("ab","eidbaooo"))
# print(checkInclusion("ab","eidboaoo"))
# print(checkInclusion("hello","ooolleoooleh"))

def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1
    
    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)
    
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1

    return matches == 26
    
        
