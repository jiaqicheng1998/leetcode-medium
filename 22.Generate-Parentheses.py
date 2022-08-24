# Given n pairs of parentheses, write a function to 
# generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

# only add open parentheses if open < n
# only add a closing parentheses if closed < open
# valid IIF open == closed == n
# because the stack is a global variable, got to clear up the stack
# 会一直反到上层 然后一直清理干净 直到分叉
def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return 
        
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
    
    backtrack(0,0)
    return res

