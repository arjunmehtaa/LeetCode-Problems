# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(node, mini, maxi):
            if not node:
                return True
            if node.val <= mini or node.val >= maxi:
                return False
            return checkBST(node.left, mini, node.val) and checkBST(node.right, node.val, maxi)
        
        return checkBST(root, -inf, inf)