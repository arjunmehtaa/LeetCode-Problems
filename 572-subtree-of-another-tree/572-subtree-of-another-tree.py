# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if isSame(root, subRoot):
            return True
        left, right = False, False
        if root.left:
            left = self.isSubtree(root.left, subRoot)
        if root.right:
            right = self.isSubtree(root.right, subRoot)
        return left or right
        
        
def isSame(root, subRoot):
    if not root and not subRoot:
        return True
    elif not root or not subRoot:
        return False
    elif root.val == subRoot.val:
        return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
    else:
        return False