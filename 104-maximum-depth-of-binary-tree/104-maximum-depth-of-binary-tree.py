# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return traverse(root)
        
def traverse(node):
    if node == None:
        return 1
    left = traverse(node.left) if node.left else 0
    right = traverse(node.right) if node.right else 0
    return 1 + max(left, right)