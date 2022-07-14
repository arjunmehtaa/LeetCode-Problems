# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getTreeHeight(root):
    node = root
    height = 0
    while node.left:
        node = node.left
        height += 1
    return height

def nodeExists(index, height, node):
    left = 0
    right = pow(2, height) - 1
    count = 0
    while count < height:
        mid = ceil((left + right) / 2)
        if index >= mid:
            node = node.right
            left = mid
        else:
            node = node.left
            right = mid - 1
        count += 1
    return node != None

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        height = getTreeHeight(root)
        if height == 0:
            return 1
        total += pow(2, height) - 1
        left = 0
        right = total
        while left < right:
            index = math.ceil((left + right) / 2)
            if nodeExists(index, height, root):
                left = index
            else:
                right = index - 1
        return total + (left + 1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        