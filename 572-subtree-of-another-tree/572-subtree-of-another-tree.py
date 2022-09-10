# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if areTreesIdentical(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
        
        
def areTreesIdentical(root, subRoot):
    if not root and not subRoot:
        return True
    if not root or not subRoot:
        return False
    if root.val != subRoot.val:
        return False
    if not areTreesIdentical(root.left, subRoot.left) or not areTreesIdentical(root.right, subRoot.right):
        return False
    return True