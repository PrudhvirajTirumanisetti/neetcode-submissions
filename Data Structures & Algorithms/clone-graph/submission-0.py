"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2New = {}

        def dfs(node):
            if not node: return 
            if node in old2New:
                return old2New[node]
            
            copy = Node(node.val)
            old2New[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)