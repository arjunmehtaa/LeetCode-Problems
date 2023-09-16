# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return traverse(root, -inf, inf)
        
def traverse(node, mini, maxi):
    if not node:
        return True
    if node.val <= mini or node.val >= maxi:
        return False
    left = traverse(node.left, mini, node.val)
    right = traverse(node.right, node.val, maxi)
    return left and right