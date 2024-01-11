# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (None, None)
            if not node.left and not node.right:
                return (node.val, node.val)
            
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)

            res_min = min(l_min if l_min is not None else float("inf"), r_min if r_min is not None else float("inf"), node.val)
            res_max = max(l_max if l_max is not None else 0, r_max if r_max is not None else 0, node.val)
            
            nonlocal res
            res = max(abs(node.val-res_min), abs(node.val-res_max), res)
            print(f"{node.val=}, {res_min=}, {res_max=}, {res=}")
            return (res_min, res_max)
        
        res = 0
        dfs(root)
        return res

        