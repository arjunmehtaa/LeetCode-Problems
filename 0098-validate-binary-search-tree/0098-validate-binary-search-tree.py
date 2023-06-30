# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return traverse(-inf, inf, root)
        
def traverse(minVal, maxVal, node):
    if node.val <= minVal or node.val >= maxVal:
        return False
    if node.left:
        if not traverse(minVal, node.val, node.left):
            return False
    if node.right:
        if not traverse(node.val, maxVal, node.right):
            return False
    return True