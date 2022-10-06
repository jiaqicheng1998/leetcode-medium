# Given a collection of candidate numbers (candidates) and a target 
# number (target), find all unique combinations in candidates where 
# the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.
def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i+1, cur, total + candidates[i])
        cur.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res