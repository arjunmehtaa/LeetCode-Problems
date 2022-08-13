# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return traverse(root, -inf, inf)
        
def traverse(root, left, right):
    if not root:
        return True
    if root.val <= left or root.val >= right:
        return False
    left = traverse(root.left, left, root.val)
    right = traverse(root.right, root.val, right)
    return left and right
