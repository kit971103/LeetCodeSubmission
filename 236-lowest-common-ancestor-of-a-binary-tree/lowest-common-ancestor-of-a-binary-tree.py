# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            
            if not node: return
            nonlocal p_path
            nonlocal q_path
            path.append(node)
            if node == p: 
                p_path = path.copy()
            if node == q: 
                q_path = path.copy()
            if p_path is not None and q_path is not None: return
            dfs(node.left)
            dfs(node.right)
            path.pop()

        path = []
        p_path = None
        q_path = None
        dfs(root)
        
        # CommonAncestor = root
        for a, b in zip(p_path, q_path):
            if a != b: break
            CommonAncestor = a
        return CommonAncestor

