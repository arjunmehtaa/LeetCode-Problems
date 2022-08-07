# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return traverse(root, -inf, inf)
        
def traverse(node, left, right):
    if node.val <= left or node.val >= right:
        return False
    l = True
    r = True
    if node.left:
        l = traverse(node.left, left, node.val)
    if node.right:
        r = traverse(node.right, node.val, right)
    if not l or not r:
        return False
    return True
    