# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node.left and not node.right:
                return (node.val, node.val)
            
            res_min = res_max = node.val
            
            if node.left:
                t_min, t_max = dfs(node.left)
                res_min  =min(res_min, t_min)
                res_max = max(res_max, t_max)
            if node.right:
                t_min, t_max = dfs(node.right)
                res_min  =min(res_min, t_min)
                res_max = max(res_max, t_max)

            nonlocal res
            res = max(abs(node.val-res_min), abs(node.val-res_max), res)
            return (res_min, res_max)
        
        res = 0
        dfs(root)
        return res

        