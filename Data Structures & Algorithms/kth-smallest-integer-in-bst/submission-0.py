# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        counter = 0
        currentNode = root

        while currentNode or stack:
            while currentNode: 
                stack.append(currentNode)
                currentNode=currentNode.left
            currentNode=stack.pop()
            counter+=1
            
            if counter == k:
                return currentNode.val
            
            currentNode=currentNode.right