# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right   

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        sub = []
        q = [root]
        size = 1
        count = 0
        while len(q):
            node = q.pop(0)
            count += 1
            sub.append(node.val)
            if node.left: 
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if count == size:
                size = len(q)
                count = 0
                res.append(sub)
                sub = []
        return res