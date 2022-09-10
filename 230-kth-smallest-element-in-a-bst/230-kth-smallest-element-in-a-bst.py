# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = 0
        
        def traverse(node):
            if node.left:
                traverse(node.left)
            self.count += 1
            if self.count == k:
                self.answer = node.val
            if node.right:
                traverse(node.right)
                
        traverse(root)
        return self.answer