# Given the root of a binary search tree, and an integer k, return the kth 
# smallest value (1-indexed) of all the values of the nodes in the tree.

def kthSmallest(root, k):

    res = []
    def dfs(root):
        if not root:
            return
        
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
        return res
    
    dfs(root)
    res.sort()
    return res[k-1]
