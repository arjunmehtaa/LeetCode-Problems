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
        ans = []
        queue = [root]
        count = 0
        size = len(queue)
        while len(queue) > 0:
            if count == size:
                count = 0
                size = len(queue)
            sub = []
            while count < size:
                count += 1
                node = queue.pop(0)
                sub.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sub)
        return ans
        