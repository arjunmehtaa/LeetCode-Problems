# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        
        def traverse(self, node):
            if node.left:
                traverse(self, node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            if node.right:
                traverse(self, node.right)
                
        traverse(self, root)
        return self.res