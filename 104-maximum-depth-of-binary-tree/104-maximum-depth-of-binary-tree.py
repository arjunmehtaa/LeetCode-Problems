# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return traverse(root)
        
def traverse(node):
    if node == None:
        return 0
    left = traverse(node.left)
    right = traverse(node.right)
    maxim = max(left, right)
    return 1 + maxim
    