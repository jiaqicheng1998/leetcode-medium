# Given the root of a binary tree, return the level order 
# traversal of its nodes' values. (i.e., from 
# left to right, level by level).

def levelOrder(root):
    res = []

    q = collections.deque()
    q.append(root)

    while q:
        qLen = len(q) #ensure us going one level at a time
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        if level:
            res.append(level)
    return res
