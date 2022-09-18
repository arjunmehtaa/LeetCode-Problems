# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.val == subRoot.val:
                if isSame(node, subRoot):
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
        
def isSame(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    else:
        if p.val == q.val:
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        else:
            return False