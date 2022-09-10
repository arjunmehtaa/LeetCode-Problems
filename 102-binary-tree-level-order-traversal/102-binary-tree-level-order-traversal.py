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
        queue = [root]
        answer = []
        size = len(queue)
        count = 0
        while len(queue) > 0:
            levelList = []
            while count < size:
                node = queue.pop(0)
                levelList.append(node.val)
                count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(levelList)
            size = len(queue)
            count = 0
        return answer
                