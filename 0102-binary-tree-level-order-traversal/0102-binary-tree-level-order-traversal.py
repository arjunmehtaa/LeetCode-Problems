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
        while len(queue):
            size = len(queue)
            tempList = []
            while size > 0:
                ele = queue.pop(0)
                size -= 1
                tempList.append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            ans.append(tempList)
        return ans