# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = [root]
        level = 0
        if not root:
            return []
        while len(queue) > 0:
            size = len(queue)
            level_nodes = []
            count = 0
            while count < size:
                count += 1
                element = queue.pop(0)
                if not element:
                    break
                level_nodes.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            ans.append(level_nodes)
        return ans
            
            