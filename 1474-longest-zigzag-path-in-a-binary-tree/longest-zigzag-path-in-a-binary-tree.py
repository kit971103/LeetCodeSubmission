# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, on_left, depth):
            if not node: return depth
            
            return max( dfs(node.left, True, (depth+1)*int(not on_left)) , dfs(node.right, False, (depth+1)*int(on_left)) )

        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))