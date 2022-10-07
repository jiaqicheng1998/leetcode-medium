# Given a string s, partition s such that every substring of the partition
#  is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:

# Input: s = "a"
# Output: [["a"]]

# bruteforce go through every partition, check if it is palindrome

def partition(s):
    res = []

    def isPal(s):
        temp = s[::-1]
        if s == temp:
            return True
        else:
            return False
    
    # subset question:
    part = []
    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        
        for j in range(i, len(s)):
            if isPal(s[i:j+1]):
                part.append(s[i:j+1])
                dfs(j+1)
                part.pop() # remember to pop, clear up the part 
    
    dfs(0)
    return res

print(partition('letter'))

s = "letter"
print(s[0:1])