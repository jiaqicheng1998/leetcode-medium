# Given two integer arrays preorder and inorder where preorder is the preorder 
# traversal of a binary tree and inorder is the inorder traversal of the same tree, 
# construct and return the binary tree.

# the first value in the preorder traversal is always going to be the root
# every value to the left of the root value in the inorder traversal is in the left
# subtree. same applies to the right 

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None 
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
    node.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])
    return root