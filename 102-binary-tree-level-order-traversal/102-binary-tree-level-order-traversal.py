# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        size = len(queue)
        sub = []
        res = []
        if not root:
            return []
        while len(queue) > 0:
            if size == 0:
                size = len(queue)
                res.append(sub)
                sub = []
            node = queue.pop(0)
            size -= 1
            sub.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(sub)
        return res