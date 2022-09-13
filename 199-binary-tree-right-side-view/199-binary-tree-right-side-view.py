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
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution using DFS
#
# Time Complexity   : O(N)
# Space Complexity  : O(N)

# def traverseTree(node, level, ans):
#     if node == None:
#         return -1
#     level += 1
#     if level > len(ans):
#         ans.append(node.val)
#     traverseTree(node.right, level, ans)
#     traverseTree(node.left, level, ans)
    
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#         traverseTree(root, 0, ans)
#         return ans

# Solution using BFS
#
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         res = []
#         queue = [root]
#         while len(queue):
#             size = len(queue)
#             count = 0
#             while count < size:
#                 node = queue.pop(0)
#                 count += 1
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(node.val)
#         return res