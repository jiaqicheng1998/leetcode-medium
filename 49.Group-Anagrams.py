# Given an array of strings strs, group the anagrams 
# together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging 
# the letters of a different word or phrase, typically 
# using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

# def groupAnagrams(strs):
#     res = [[strs.pop()]]
#     isInsert = False

#     while strs:
#         curr = strs.pop()
#         for i in range(len(res)):
#             if isAnagrams(curr, res[i][0]):
#                 res[i].append(curr)
#                 isInsert = True
#                 break
#         if not isInsert:
#             res.append([curr])
        

#     return res

# def isAnagrams(s,t):
#     d = {}
#     for i in s:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1

#     for j in t:
#         if j in d:
#             d[j] -= 1
#         else:
#             return False

#     for m in d.values():
#         if m != 0:
#             return False
#     return True 
from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list) # mapping charCount to list of Anagrams

    for s in strs:
        count = [0] * 26 # a ... z

        for c in s:
            count[ord(c) - ord('a')] += 1 

        res[tuple(count)].append(s)
    
    return res.values()


print(groupAnagrams(["a"]))
print(groupAnagrams([""]))
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))