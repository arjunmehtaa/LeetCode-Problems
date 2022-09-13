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
        answer = []
        seen = set()
        
        def traverse(node, level):
            if level not in seen:
                seen.add(level)
                answer.append(node.val)
            if node.right:
                traverse(node.right, level + 1)
            if node.left:
                traverse(node.left, level + 1)
            
        traverse(root, 1)
        return answer