# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if isSameTree(root, subRoot):
            return True
        if root.left and self.isSubtree(root.left, subRoot):
            return True
        if root.right and self.isSubtree(root.right, subRoot):
            return True
        return False
        
def isSameTree(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False
    if not isSameTree(a.left, b.left) or not isSameTree(a.right, b.right):
        return False
    return True
    