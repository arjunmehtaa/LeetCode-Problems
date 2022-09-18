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
        return traverse(root, -inf, inf)
        
def traverse(node, minLimit, maxLimit):
    if node.val <= minLimit or node.val >= maxLimit:
        return False
    left, right = True, True
    if node.left:
        left = traverse(node.left, minLimit, node.val)
    if node.right:
        right = traverse(node.right, node.val, maxLimit)
    return left and right