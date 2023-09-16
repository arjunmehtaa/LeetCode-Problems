# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = k
        self.ans = root.val
            
        def traverse(node, value):
            if node.left:
                traverse(node.left, value)
            self.counter -= 1
            if self.counter  == 0:
                self.ans = node.val
            if node.right:
                traverse(node.right, value)
        
        traverse(root, k)
        return self.ans
        