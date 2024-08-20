# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.res = root.val
        
        def traverse(node):
            if node.left:
                traverse(node.left)
            self.i += 1
            if self.i == k:
                self.res = node.val
            if node.right:
                traverse(node.right)
                
        traverse(root)
        return self.res
            
        