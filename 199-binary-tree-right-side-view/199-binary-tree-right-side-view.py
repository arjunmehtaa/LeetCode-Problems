# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        while len(q):
            sub = []
            size = len(q)
            count = 0
            while count < size:
                node = q.pop(0)
                sub.append(node.val)
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sub[len(sub) - 1])
        return res