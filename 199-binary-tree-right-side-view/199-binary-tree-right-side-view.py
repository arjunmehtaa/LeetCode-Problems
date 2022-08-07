# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        traverse(root, 0, ans)
        return ans
        
def traverse(node, level, ans):
    if not node:
        return
    level += 1
    if level > len(ans):
        ans.append(node.val)
    traverse(node.right, level, ans)
    traverse(node.left, level, ans)
    
    
        