# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isValid(root, -inf, inf)
        
def isValid(node, mini, maxi):
    if not node:
        return True
    if node.val >= maxi or node.val <= mini:
        return False
    return isValid(node.left, mini, node.val) and isValid(node.right, node.val, maxi)
            