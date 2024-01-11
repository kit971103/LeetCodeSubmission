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
            elif not node.left:
                r_min, r_max = dfs(node.right)
                res_min = min(r_min , node.val)
                res_max = max(r_max , node.val)
            elif not node.right:
                l_min, l_max = dfs(node.left)
                res_min = min(l_min, node.val)
                res_max = max(l_max, node.val)
            else:
                l_min, l_max = dfs(node.left)
                r_min, r_max = dfs(node.right)
                res_min = min(l_min, r_min , node.val)
                res_max = max(l_max, r_max , node.val)
            
            nonlocal res
            res = max(abs(node.val-res_min), abs(node.val-res_max), res)
            return (res_min, res_max)
        
        res = 0
        dfs(root)
        return res

        