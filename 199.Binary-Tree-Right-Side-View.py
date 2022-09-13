# Given the root of a binary tree, imagine yourself standing on the 
# right side of it, return the values of the nodes you can see ordered 
# from top to bottom.

def rightSideView(root):
    res = []
    q = collections.deque()
    q.append(root)
    if not root:
        return []
    while q:
        qLen = len(q)
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
            res.append(level[-1])
    return res

