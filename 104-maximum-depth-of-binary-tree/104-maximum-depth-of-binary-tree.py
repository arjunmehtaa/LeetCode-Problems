# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverseTree(node, level):
    if node == None:
        return level-1
    left = traverseTree(node.left, level+1)
    right = traverseTree(node.right, level+1)
    return max(left, right)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return traverseTree(root, 1)
        