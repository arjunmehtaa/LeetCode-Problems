# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        
        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            left = max(left, 0)
            right = max(right, 0)
            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)
            
        traverse(root)
        return self.ans
