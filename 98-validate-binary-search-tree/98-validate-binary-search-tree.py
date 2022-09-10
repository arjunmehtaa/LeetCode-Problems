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
    if node.val <= mini or node.val >= maxi:
        return False
    if node.left:
        if not traverse(node.left, mini, node.val):
            return False
    if node.right:
        if not traverse(node.right, node.val, maxi):
            return False
    return True